# Generated by Django 3.2.9 on 2021-12-08 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coverletters', '0013_coverletter_selected_texfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coverletter',
            name='selected_texfile',
        ),
    ]