from django.db import models


def upload_update_image(instance, filename):
    return f"static/image/{filename}"


# Create your models here.
class Image(models.Model):
    id = models.BigAutoField(primary_key=True)
    src = models.ImageField(upload_to=upload_update_image, blank=False, null=False)
    alt = models.CharField(max_length=254, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'image'

    def __str__(self):
        return self.alt
