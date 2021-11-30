# Generated by Django 3.2.9 on 2021-11-30 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('coverletters', '0004_auto_20211130_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coverletter',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coverletters', to='sessions.session'),
        ),
    ]
