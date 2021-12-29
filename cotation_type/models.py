from django.db import models


class CotationType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cotation_type'


