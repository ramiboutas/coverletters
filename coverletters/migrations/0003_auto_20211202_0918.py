# Generated by Django 3.2.9 on 2021-12-02 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coverletters', '0002_auto_20211201_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coverletter',
            name='company_city',
        ),
        migrations.RemoveField(
            model_name='coverletter',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='coverletter',
            name='company_recruiter',
        ),
        migrations.RemoveField(
            model_name='coverletter',
            name='company_street_no',
        ),
        migrations.RemoveField(
            model_name='coverletter',
            name='company_zip_code',
        ),
        migrations.AddField(
            model_name='coverletter',
            name='company_text',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coverletter',
            name='candidate_email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]
