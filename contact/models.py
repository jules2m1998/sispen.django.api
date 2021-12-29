from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=12, validators=[RegexValidator(r'^\d{0,12}$')], default=0)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'contact'

    def __str__(self):
        return self.email
