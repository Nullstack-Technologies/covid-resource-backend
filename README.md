# Khidmat Covid Resources and Relief Management Portal

Version 1.0

### Getting Started


#### 1. Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ virtualenv -p /usr/bin/python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

#### 2. Add a file secret.py file parallel to settings.py and add the following settings(As you wish)
 
 ```python

# OVERRIDE SECRET KEY
SECRET_KEY = 'nauman!kl+aprbgu#m(kj!@_*i5g!ve-9(u*m+wfr^!xsnarif'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'khidmat',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.domain.com'
# EMAIL_PORT = 500
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''


```

### Migrate 

```bash
python manage.py migrate
```

### Run the Project
```bash
python manage.py runserver
```

## Company

### NullStack Technologies
<a href="https://nullstacks.com"><img src="https://nullstacks.com/wp-content/uploads/2019/04/Nullstack-icon-150x150.png" /></a>

## Author(s)

👤 **Nauman Arif**

- LinkedIn: [@naumanarif21](https://www.linkedin.com/in/nauman-arif/)
- Github: [@naumanarif21](https://github.com/naumanarif21)

## Show your support

Please ⭐️ this repository if this project helped you!

Thank You!!!
