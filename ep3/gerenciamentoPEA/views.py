from django.shortcuts import render
from django.http import HttpResponse
from .models import Paciente
from .models import Amostra
from .models import Exame
from .models import Paciente_exame_amostra
from django.template import loader
# Create your views here.

def index(request):
    context = {}
    template = loader.get_template('gerenciamentoPEA/index.html')
    return HttpResponse(template.render(context, request))

def pacientes(request):
    paciente_list = Paciente.objects.order_by('cpf')
    context = {
        'paciente_list': paciente_list,
    }
    return render(request, 'gerenciamentoPEA/pacientes.html', context)

def paciente_detail(request, id_paciente):
    return HttpResponse("Você está olhando para o paciente %s." % id_paciente)

def exames_do_paciente(request, id_paciente):
    response = "Você está olhando para os exames do paciente %s."
    return HttpResponse(response % id_paciente)

def faz_exame(request, id_paciente):
    return HttpResponse("Você está adicionando exame do paciente %s." % id_paciente)