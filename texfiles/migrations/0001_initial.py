# Generated by Django 3.2.9 on 2021-12-01 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TexFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('file', models.FileField(upload_to='texfiles')),
                ('cls', models.FileField(blank=True, null=True, upload_to='texfiles')),
                ('image', models.ImageField(upload_to='texfiles/screenshots')),
                ('is_active', models.BooleanField(default=True)),
                ('credits', models.CharField(blank=True, max_length=128, null=True)),
                ('credits_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
