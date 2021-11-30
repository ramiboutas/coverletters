# Generated by Django 3.2.9 on 2021-11-30 04:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('coverletters', '0002_coverletter_sessionid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coverletter',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]