# Generated by Django 3.1 on 2020-08-20 12:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_dataexport'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dataexport',
            options={'verbose_name': 'Esportazione dati', 'verbose_name_plural': 'Esportazione dati'},
        ),
        migrations.RenameField(
            model_name='pallet',
            old_name='type',
            new_name='kind',
        ),
        migrations.AddField(
            model_name='ddt',
            name='creation_time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Orario creazione'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='pallet',
            unique_together={('ddt', 'kind')},
        ),
    ]
