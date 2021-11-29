from django.db import models

# Create your models here.


class TemplateFile(models.Model):
    name = models.CharField(max_length=128)
    file = models.FileField(upload_to='templatefiles')

    def __str__(self):
        return self.name
