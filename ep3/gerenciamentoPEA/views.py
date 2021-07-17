from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Paciente, Paciente_exame_amostra, Exame, Amostra
from django.template import loader
# Create your views here.

def index(request):
    template = loader.get_template('gerenciamentoPEA/index.html')
    return render(request, 'gerenciamentoPEA/index.html', {})

def pacientes(request):
    paciente_list = Paciente.objects.order_by('cpf')
    return render(request, 'gerenciamentoPEA/pacientes.html', {'paciente_list': paciente_list})

def paciente_detail(request, id_paciente):
    paciente = get_object_or_404(Paciente, pk=id_paciente)
    return render(request, 'gerenciamentoPEA/paciente_detalhes.html', {'paciente': paciente})

def exames_do_paciente(request, id_paciente):
    response = "Você está olhando para os exames do paciente %s."
    return HttpResponse(response % id_paciente)

def faz_exame(request, id_paciente):
    return HttpResponse("Você está adicionando exame do paciente %s." % id_paciente)