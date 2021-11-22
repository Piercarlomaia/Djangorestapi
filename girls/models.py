from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        cria um usuario dado email e senha.
        """
        if not email:
            raise ValueError('O usuario deve ter um email')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_professor(self, email, password):
        """
        cria um professor dado usuario e senha
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.professor = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        cria um admin dado usuario e senha
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.professor = True
        user.is_staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User2(AbstractBaseUser):

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    Nome = models.CharField(max_length=300)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    professor = models.BooleanField(default=False) # professor ?
    admin = models.BooleanField(default=False) # a superuser



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] #email e password sao default

    def get_full_name(self):
        # o usuario e identificado pelo nome
        return self.nome

    def get_email(self):
        # o usuario e identificado pelo email
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True



    @property
    def is_professor(self):
        "o usuario e professor ?"
        return self.professor

    @property
    def is_admin(self):
        "o usuario e admin ?"
        return self.admin

    objects = UserManager()


class aulas(models.Model):
    professor = models.ForeignKey(User2, on_delete=models.CASCADE)
    Nome = models.CharField(max_length=300)
    descricao = models.TextField(max_length=500)
    categoria = models.CharField(max_length=300)
    datadepublicacao = models.DateTimeField(auto_now_add=True)
    datadeedicao = models.DateTimeField(auto_now=True)
    link = models.URLField(max_length=300)
    def __str__(self):
        return self.Nome


class cursos(models.Model):
    usuarios = models.ManyToManyField(User2, related_name='users', blank=True)
    professores = models.ManyToManyField(User2, related_name='profs')
    aulas = models.ManyToManyField(aulas)
    Nome = models.CharField(max_length=300)
    descricao = models.TextField(max_length=500)
    categoria = models.CharField(max_length=300)
    datadepublicacao = models.DateTimeField(auto_now_add=True)
    datadeedicao = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.Nome

