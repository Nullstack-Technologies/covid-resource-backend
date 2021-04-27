from rolepermissions.roles import AbstractUserRole


class Entity(AbstractUserRole):
    pass


class Verifier(AbstractUserRole):
    pass


class Admin(AbstractUserRole):
    pass
