from django.db import models
from django.core.files.storage import FileSystemStorage
from django.dispatch import receiver
from django.db.models.signals import post_delete

from utils.files import delete_path_file

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
    downloads = models.IntegerField(default=0)

    def __str__(self):
        return self.name


@receiver(post_delete, sender=TexFile)
def delete_tex_file(sender, instance, **kwargs):
    if instance.file:
        delete_path_file(instance.file.path)
