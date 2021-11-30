# Generated by Django 3.2.9 on 2021-11-30 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coverletters', '0003_alter_coverletter_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='session key')),
                ('session_data', models.TextField(verbose_name='session data')),
                ('expire_date', models.DateTimeField(db_index=True, verbose_name='expire date')),
            ],
            options={
                'verbose_name': 'session',
                'verbose_name_plural': 'sessions',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='coverletter',
            name='session',
            field=models.ForeignKey(default='afasdf', on_delete=django.db.models.deletion.CASCADE, related_name='coverletters', to='coverletters.customsession'),
            preserve_default=False,
        ),
    ]