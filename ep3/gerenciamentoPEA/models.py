from django.db import models
from django.db.models.fields import DateField

# Create your models here.

class Paciente(models.Model):
    id_paciente = models.IntegerField(primary_key=True)
    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    nascimento = models.DateField()

class Exame(models.Model):
    id_exame = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=255)
    virus = models.CharField(max_length=255)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('tipo', 'virus',)

class Amostra(models.Model):
    id_amostra = models.IntegerField(primary_key=True)
    codigo_amostra = models.CharField(max_length=255, unique=True)
    metodo_de_coleta = models.CharField(max_length=255)
    material = models.CharField(max_length=255)

class Paciente_exame_amostra(models.Model):
    id_paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    id_exame = models.OneToOneField(Exame, on_delete=models.CASCADE)
    id_amostra = models.OneToOneField(Amostra, on_delete=models.CASCADE)
    data_de_realizacao = models.DateTimeField()
    data_de_solicitacao = models.DateTimeField()
    class Meta:
        unique_together = ('id_paciente', 'id_exame', 'id_amostra', 'data_de_realizacao')