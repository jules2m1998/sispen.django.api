from django.core.validators import RegexValidator
from django.db import models
from django.conf import settings
from description.models import Description
from image.models import Image


class Partner(models.Model):
    partner_name = models.CharField(max_length=250, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    url = models.CharField(max_length=250, unique=True)
    phone = models.CharField(max_length=12, validators=[RegexValidator(r'^\d{0,12}$')], default=0)
    localisation = models.CharField(max_length=250, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    img = models.OneToOneField(Image, on_delete=models.CASCADE)
    description = models.OneToOneField(Description, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'partner'
        ordering = ['partner_name']

    def __str__(self):
        return self.partner_name
