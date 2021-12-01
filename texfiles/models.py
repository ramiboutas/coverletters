from django.db import models


class TexFile(models.Model):
    name = models.CharField(max_length=128)
    file = models.FileField(upload_to='texfiles')
    cls = models.FileField(upload_to='texfiles', blank=True, null=True)
    image = models.ImageField(upload_to='texfiles/screenshots')
    is_active = models.BooleanField(default=True)
    credits = models.CharField(max_length=128, blank=True, null=True)
    credits_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
