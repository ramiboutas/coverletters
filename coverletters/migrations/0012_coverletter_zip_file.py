# Generated by Django 3.2.9 on 2021-12-05 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coverletters', '0011_auto_20211204_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='coverletter',
            name='zip_file',
            field=models.FileField(blank=True, null=True, upload_to='zipfiles/%Y/%m/%d'),
        ),
    ]
