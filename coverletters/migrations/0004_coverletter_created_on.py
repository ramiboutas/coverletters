# Generated by Django 3.2.9 on 2021-12-02 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coverletters', '0003_auto_20211202_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='coverletter',
            name='created_on',
            field=models.DateField(auto_now=True),
        ),
    ]