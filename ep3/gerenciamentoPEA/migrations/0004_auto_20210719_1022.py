# Generated by Django 3.2.5 on 2021-07-19 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamentoPEA', '0003_paciente_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exame',
            name='tipo',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='exame',
            name='virus',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='paciente_exame_amostra',
            name='data_de_realizacao',
            field=models.DateTimeField(),
        ),
        migrations.AlterUniqueTogether(
            name='exame',
            unique_together={('tipo', 'virus')},
        ),
        migrations.AlterUniqueTogether(
            name='paciente_exame_amostra',
            unique_together={('id_paciente', 'id_exame', 'id_amostra', 'data_de_realizacao')},
        ),
    ]