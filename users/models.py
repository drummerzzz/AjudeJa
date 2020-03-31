from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.conf import settings
from django.core.mail import send_mail


class BaseUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
    Username and password are required. Other fields are optional.
    """
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        'Nome de Usuario',
        max_length=20,
        unique=True,
        help_text=(
            'O nome de usuario deve conter ate 20 caracteres sendo estes letras, números ou @/./+/-/_ somente.'),
        validators=[username_validator],
        error_messages={
            'unique': ("Já existe um usuario com esse nome."),
        },
        blank=True,
    )

    email = models.EmailField('Endereço de e-mail', unique=True,
                help_text='Ja existe um usuario com esse e-mail')

    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text=('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        'usuario status',
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    create_at = models.DateTimeField('Data de Inicio', auto_now_add=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_level(self):
        return self.nivel

    def set_level(self, level):
        self.nivel = level

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        """Return the short name for the user."""
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_username(self):
        return self.username

    def get_staff(self):
        return self.is_staff

    def __str__(self):
        return self.username
        
    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
        abstract = True


class User(BaseUser):

    class Meta(BaseUser.Meta):
        swappable = 'AUTH_USER_MODEL'

