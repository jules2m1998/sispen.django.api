from django.db import models
from description.models import Description


class Cotation(models.Model):
    name = models.CharField(max_length=250, unique=True)
    cotation_type = models.ForeignKey('cotation_type.CotationType', on_delete=models.CASCADE, null=True, blank=True)
    description = models.ForeignKey(Description, on_delete=models.CASCADE)
    parent = models.ForeignKey('Cotation', on_delete=models.CASCADE, null=True, blank=True)
    is_last = models.BooleanField(default=False)
    price = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cotation'
        ordering = ['name']
