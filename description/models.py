from django.db import models


# Create your models here.
class Description(models.Model):
    fr = models.CharField(max_length=254, null=False)
    en = models.CharField(max_length=254, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'description'
