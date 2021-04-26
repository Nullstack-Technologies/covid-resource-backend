import pyotp
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core import exceptions
import django.contrib.auth.password_validation as validators
from django.core.validators import RegexValidator
from django.http import Http404

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rolepermissions.roles import assign_role

from authentication.models import Customer
from communication.tasks import send_sms
from generic.models import Address
from generic.regular_expressions import phone_number_validator_regex
from generic.serializers import AuditSerializer

User = get_user_model()


class RegistrationSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=100)
    mobile_number = serializers.CharField(
        validators=[
            RegexValidator(phone_number_validator_regex),
        ],
        max_length=13,
    )

    def validate(self, attrs):
        attrs['user_permissions'] = None
        attrs['token'] = ''

        profile = Customer.objects.filter(
            mobile_number=attrs['mobile_number']
        )
        if profile:
            profile = profile[0]
            if not profile.user.is_active:
                raise serializers.ValidationError({
                    'mobile_number': 'Mobile Number Exists, Please try logging in!',
                    'verification_required': True
                })
            else:
                raise serializers.ValidationError({
                    'mobile_number': 'Mobile Number Exists, Please try logging in!',
                    'verification_required': False
                })

        return super().validate(attrs)

    def create(self, validated_data):

        request = self.context.get('request')
        user = User.objects.create_user(
            username=validated_data.get('mobile_number'),
            first_name=validated_data.get('name'),
            is_active=False
        )
        assign_role(user, 'customer')
        profile = Customer.objects.create(
            user=user,
            mobile_number=validated_data.get('mobile_number'),
            base32_hash=pyotp.random_base32()
        )
        otp = profile.generate_otp()

        send_sms.delay(settings.OTP_TEXT_FOR_SENDING % otp, profile.mobile_number)
        return validated_data


class RequestOTPSerializer(serializers.Serializer):

    mobile_number = serializers.CharField(
        validators=[RegexValidator(phone_number_validator_regex)],
        max_length=13,
    )
    otp = serializers.CharField(max_length=6, min_length=6, read_only=True)

    def validate(self, attrs):

        mobile_number = attrs.get('mobile_number')

        profile = Customer.objects.filter(
            mobile_number=mobile_number,
        )
        if profile:
            profile = profile[0]
            # if profile.user.is_active:
            #     raise serializers.ValidationError({
            #         'otp': 'Account has already been verified!',
            #     })
            attrs['profile'] = profile
        else:
            raise Http404

        return super().validate(attrs)

    def create(self, validated_data):
        profile = validated_data.get('profile')
        otp = profile.generate_otp()
        send_sms.delay(settings.OTP_TEXT_FOR_SENDING % otp, profile.mobile_number)
        return validated_data


class VerifyOTPSerializer(serializers.Serializer):

    mobile_number = serializers.CharField(
        validators=[RegexValidator(phone_number_validator_regex)],
        max_length=13,
    )
    otp = serializers.CharField(max_length=6, min_length=6, write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, attrs):

        mobile_number = attrs.get('mobile_number')
        otp = attrs.get('otp')

        profile = Customer.objects.filter(
            mobile_number=mobile_number,
        )
        if profile:
            profile = profile[0]
            if not profile.verify_otp(otp):
                raise serializers.ValidationError({
                    'otp': 'One Time Password has expired or is incorrect',
                })
            profile.user.is_active = True
            profile.user.save()
            attrs['profile'] = profile
        else:
            raise Http404

        return super().validate(attrs)

    def create(self, validated_data):
        profile = validated_data.get('profile')
        token, created = Token.objects.get_or_create(user=profile.user)
        validated_data['token'] = token
        return validated_data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = (
            "id",
            "password",
            "last_login",
            "is_superuser",
            "email",
            "groups",
            "user_permissions",
            "is_staff",
            "is_active",
            "username"
        )


class ProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Customer
        fields = (
            'user',
            'mobile_number'
        )


class AddressSerializer(AuditSerializer):
    distance_from_pin_point = serializers.FloatField(read_only=True)

    class Meta:
        model = Address
        exclude = (
            'status',
        )
