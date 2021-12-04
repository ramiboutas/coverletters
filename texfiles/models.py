from django.db import models
from django.core.files.storage import FileSystemStorage
cls_storage = FileSystemStorage(location='/home/rami/texmf/tex/latex/local')


class TexFile(models.Model):
    name = models.CharField(max_length=128)
    file = models.FileField(upload_to='texfiles')
    cls = models.FileField(storage=cls_storage, blank=True, null=True)
    interpreter = models.CharField(max_length=20, default='lualatex')
    image = models.ImageField(upload_to='tex_screenshots')
    is_active = models.BooleanField(default=True)
    credits = models.CharField(max_length=128, blank=True, null=True)
    credits_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
