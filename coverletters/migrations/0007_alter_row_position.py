# Generated by Django 3.2.9 on 2021-12-03 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coverletters', '0006_auto_20211203_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='row',
            name='position',
            field=models.SmallIntegerField(),
        ),
    ]
