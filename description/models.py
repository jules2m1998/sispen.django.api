from django.db import models
from util.utils import DefaultModel


# Create your models here.
class Description(DefaultModel, models.Model):
    id = models.BigAutoField(primary_key=True)
    fr = models.CharField(max_length=254, null=False)
    en = models.CharField(max_length=254, null=True)

    class Meta:
        db_table = 'description'
