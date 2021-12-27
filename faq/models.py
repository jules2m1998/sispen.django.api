from django.conf import settings
from django.db import models


# Create your models here.
class FAQ(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.CharField(max_length=250, unique=True)
    answer = models.CharField(max_length=250, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'faq'
        ordering = ['id']

    def __str__(self):
        return self.question
