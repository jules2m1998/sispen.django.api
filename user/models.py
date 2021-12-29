from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


# Create your models here.
class User(AbstractUser):
    Male = 'Male'
    Female = 'Female'
    Sex = [(Male, 'Male'), (Female, 'Female')]

    email = models.EmailField(verbose_name="email", max_length=254, unique=True)
    cni = models.CharField(unique=True, max_length=14, default=1, validators=[RegexValidator(r'^\d{1,14}$')])
    phone = models.CharField(max_length=12, validators=[RegexValidator(r'^\d{0,12}$')], default=0)
    sex = models.CharField(max_length=10, choices=Sex, default=Male, )
    dob = models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS = ['first_name', 'phone', 'username', 'password', 'cni', 'sex', 'is_active']

    USERNAME_FIELD = "email"

    class Meta:
        db_table = 'user'

    def get_username(self):
        return self.email

    def __str__(self):
        return self.email
