from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models

# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, phone, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, phone, 
        date_of_birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        
        user = self.model(
            email=self.normalize_email(email),
            phone=phone, 
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, phone, date_of_birth=None, password=None):
        user = self.create_user(
            email=email,
            password=password,
            phone=phone,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUserModel(AbstractBaseUser):
    email = models.EmailField(verbose_name="Email Address", max_length=254, unique=True)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone", "date_of_birth"]

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True
    
    def has_module_perms(self, app_label):
        "Does the user have permission to view the app_label?"
        return True
