from django.db import models
from app.cliente.models import Cliente
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)



class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Tecnico(models.Model):
    id_tec = models.CharField(primary_key=True, max_length=12, editable=False)
    nom_tec = models.CharField(max_length=150, verbose_name="Nombre completo", null=False, help_text="Nombre completo del tecnico")

    def __str__(self):
        return self.nom_tec

class Asignar(models.Model):
    id_as = models.CharField(primary_key=True, max_length=12)
    fk_tec = models.ManyToManyField(User, verbose_name="Tecnico a Asignar", help_text="Tecnico que se le asignara Cliente")
    fk_cli = models.ManyToManyField(Cliente, verbose_name="Cliente Asignado", help_text="Cliente que pidio orden")

    def __str__ (self):
        return self.id_as
