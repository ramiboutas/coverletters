from django.db import models




class TexFile(models.Model):
    name = models.CharField(max_length=128)
    file = models.FileField(upload_to='texfiles')
    image = models.ImageField(upload_to='texfiles')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
