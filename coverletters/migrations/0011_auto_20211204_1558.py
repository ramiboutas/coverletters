# Generated by Django 3.2.9 on 2021-12-04 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coverletters', '0010_auto_20211203_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coverletter',
            name='candidate_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='coverletter',
            name='candidate_website',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]