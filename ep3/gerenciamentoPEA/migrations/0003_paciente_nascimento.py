# Generated by Django 3.2.5 on 2021-07-17 19:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamentoPEA', '0002_paciente_exame_amostra_data_de_solicitacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='nascimento',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
