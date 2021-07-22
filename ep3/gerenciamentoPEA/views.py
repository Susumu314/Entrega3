from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Paciente, Paciente_exame_amostra, Exame, Amostra
from django.template import loader
from django.urls import reverse
from datetime import datetime
# Create your views here.

def index(request):
    template = loader.get_template('gerenciamentoPEA/index.html')
    return render(request, 'gerenciamentoPEA/index.html', {})

# Paciente

def pacientes(request):
    paciente_list = Paciente.objects.order_by('cpf')
    return render(request, 'gerenciamentoPEA/pacientes.html', {'paciente_list': paciente_list})

def paciente_detail(request, id_paciente):
    paciente = get_object_or_404(Paciente, pk=id_paciente)
    return render(request, 'gerenciamentoPEA/paciente_detalhes.html', {'paciente': paciente})

def add_paciente(request):
    return render(request, 'gerenciamentoPEA/add_paciente.html', {})

def save_paciente(request):
    try:
        p = Paciente(id_paciente=request.POST['id_paciente'], cpf=request.POST['cpf'], nome=request.POST['nome'], endereco=request.POST['endereco'], nascimento=request.POST['nascimento'])
    except (KeyError):
        # Redisplay the question voting form.
        return render(request, 'gerenciamentoPEA/add_paciente.html', {
            'error_message': "Deu erro para cadastrar o paciente",
        })
    else:
        p.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return render(request, 'gerenciamentoPEA/save_paciente.html', {'paciente': p})

def change_paciente(request, id_paciente):
    paciente = get_object_or_404(Paciente, pk=id_paciente)
    return render(request, 'gerenciamentoPEA/change_paciente.html', {'paciente': paciente})

def delete_paciente(request, id_paciente):
    Paciente.objects.filter(id_paciente=id_paciente).delete()
    return render(request, 'gerenciamentoPEA/delete_paciente.html', {})

# Exames

def exames(request):
    exame_list = Exame.objects.order_by('id_exame')
    return render(request, 'gerenciamentoPEA/exames.html', {'exame_list': exame_list})

def add_exame(request):
    paciente_list = Paciente.objects.order_by('id_paciente')
    return render(request, 'gerenciamentoPEA/add_exame.html', {'paciente_list': paciente_list})

def exame_detail(request, id_exame):
    exame = get_object_or_404(Exame, pk=id_exame)
    return render(request, 'gerenciamentoPEA/exame_detalhes.html', {'exame': exame})

def exames_do_paciente(request, id_paciente):
    response = "Você está olhando para os exames do paciente %s."
    return HttpResponse(response % id_paciente)

def save_exame(request):
    try:
        p = get_object_or_404(Paciente, pk=request.POST['id_paciente'])
        try:
            Exame.objects.filter(id_exame=request.POST['id_exame']).delete()
        except:
            pass
        p.exame_set.create(id_exame=request.POST['id_exame'], tipo=request.POST['tipo'], virus=request.POST['virus'])
    except (KeyError):
        # Redisplay the question voting form.
        return render(request, 'gerenciamentoPEA/add_exame.html', {
            'error_message': "Deu erro para cadastrar o exame",
        })
    else:
        p.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return render(request, 'gerenciamentoPEA/save_exame.html', {'paciente': p})
    
def change_exame(request, id_exame):
    exame = get_object_or_404(Exame, pk=id_exame)
    paciente_list = Paciente.objects.order_by('id_paciente')
    return render(request, 'gerenciamentoPEA/change_exame.html', {'exame': exame, 'paciente_list':paciente_list})

def delete_exame(request, id_exame):
    Exame.objects.filter(id_exame=id_exame).delete()
    return render(request, 'gerenciamentoPEA/delete_exame.html', {})

# Amostra

def amostras(request):
    amostra_list = Amostra.objects.order_by('id_amostra')
    return render(request, 'gerenciamentoPEA/amostras.html', {'amostra_list': amostra_list})

def amostra_detail(request, id_amostra):
    amostra = get_object_or_404(Amostra, pk=id_amostra)
    return render(request, 'gerenciamentoPEA/amostra_detalhes.html', {'amostra': amostra})

def add_amostra(request):
    return render(request, 'gerenciamentoPEA/add_amostra.html', {})

def save_amostra(request):
    try:
        a = Amostra(id_amostra=request.POST['id_amostra'], codigo_amostra=request.POST['codigo_amostra'], metodo_de_coleta=request.POST['metodo_de_coleta'], material=request.POST['material'])
    except (KeyError):
        # Redisplay the question voting form.
        return render(request, 'gerenciamentoPEA/add_amostra.html', {
            'error_message': "Deu erro para cadastrar a amostra",
        })
    else:
        a.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return render(request, 'gerenciamentoPEA/save_amostra.html', {'amostra': a})

def change_amostra(request, id_amostra):
    amostra = get_object_or_404(Amostra, pk=id_amostra)
    return render(request, 'gerenciamentoPEA/change_amostra.html', {'amostra': amostra})

def delete_amostra(request, id_amostra):
    Amostra.objects.filter(id_amostra=id_amostra).delete()
    return render(request, 'gerenciamentoPEA/delete_amostra.html', {})

# Agregado Paciente_exame_amostra

def agregadoPEAs(request):
    agregadoPEA_list = Paciente_exame_amostra.objects.order_by('id')
    return render(request, 'gerenciamentoPEA/agregadoPEAs.html', {'agregadoPEA_list': agregadoPEA_list})

def add_agregadoPEA(request):
    paciente_list = Paciente.objects.order_by('id_paciente')
    exame_list = Exame.objects.order_by('id_exame')
    amostra_list = Amostra.objects.order_by('id_amostra')
    return render(request, 'gerenciamentoPEA/add_agregadoPEA.html', {'paciente_list': paciente_list,'amostra_list': amostra_list,'exame_list': exame_list})

def agregadoPEA_detail(request, id_agregadoPEA):
    agregadoPEA = get_object_or_404(Paciente_exame_amostra, pk=id_agregadoPEA)
    return render(request, 'gerenciamentoPEA/agregadoPEA_detalhes.html', {'agregadoPEA': agregadoPEA})

def save_agregadoPEA(request):
    paciente = get_object_or_404(Paciente, pk=request.POST['id_paciente'])
    exame = get_object_or_404(Exame, pk=request.POST['id_exame'])
    amostra = get_object_or_404(Amostra, pk=request.POST['id_amostra'])
    try:
        try:#se ja existir o agregado, deleta e atualiza as informações
            Paciente_exame_amostra.objects.filter(id_paciente=paciente, id_exame=exame, id_amostra=amostra).delete()
        except:
            pass
        ag = Paciente_exame_amostra(id_paciente=paciente, id_exame=exame, id_amostra=amostra, data_de_realizacao=(request.POST['data_de_realizacao_0'] + ' ' + request.POST['data_de_realizacao_1']), data_de_solicitacao=(request.POST['data_de_solicitacao_0']+' '+request.POST['data_de_solicitacao_1']))
    except (KeyError):
        return render(request, 'gerenciamentoPEA/add_agregadoPEA.html', {
            'error_message': "Deu erro para cadastrar o Paciente_exame_amostra",
        })
    else:
        ag.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return render(request, 'gerenciamentoPEA/save_agregadoPEA.html', {'paciente': ag})
    
def change_agregadoPEA(request, id_agregadoPEA):
    paciente_list = Paciente.objects.order_by('id_paciente')
    exame_list = Exame.objects.order_by('id_exame')
    amostra_list = Amostra.objects.order_by('id_amostra')
    agregadoPEA = get_object_or_404(Paciente_exame_amostra, pk=id_agregadoPEA)
    return render(request, 'gerenciamentoPEA/change_agregadoPEA.html', {'agregadoPEA':agregadoPEA, 'paciente_list': paciente_list,'amostra_list': amostra_list,'exame_list': exame_list})

def delete_agregadoPEA(request, id_agregadoPEA):
    Paciente_exame_amostra.objects.filter(id=id_agregadoPEA).delete()
    return render(request, 'gerenciamentoPEA/delete_agregadoPEA.html', {})