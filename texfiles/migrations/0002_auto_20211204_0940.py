# Generated by Django 3.2.9 on 2021-12-04 09:40

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texfiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='texfile',
            name='interpreter',
            field=models.CharField(default='lualatex', max_length=20),
        ),
        migrations.AlterField(
            model_name='texfile',
            name='cls',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/rami/texmf/tex/latex/local'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='texfile',
            name='image',
            field=models.ImageField(upload_to='tex_screenshots'),
        ),
    ]
