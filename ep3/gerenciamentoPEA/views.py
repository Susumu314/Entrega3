from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Paciente, Paciente_exame_amostra, Exame, Amostra
from django.template import loader
from django.urls import reverse
# Create your views here.

def index(request):
    template = loader.get_template('gerenciamentoPEA/index.html')
    return render(request, 'gerenciamentoPEA/index.html', {})

def pacientes(request):
    paciente_list = Paciente.objects.order_by('cpf')
    return render(request, 'gerenciamentoPEA/pacientes.html', {'paciente_list': paciente_list})

def exames(request):
    exame_list = Exame.objects.order_by('id_exame')
    return render(request, 'gerenciamentoPEA/exames.html', {'exame_list': exame_list})

def paciente_detail(request, id_paciente):
    paciente = get_object_or_404(Paciente, pk=id_paciente)
    return render(request, 'gerenciamentoPEA/paciente_detalhes.html', {'paciente': paciente})

def exame_detail(request, id_exame):
    exame = get_object_or_404(Exame, pk=id_exame)
    return render(request, 'gerenciamentoPEA/exame_detalhes.html', {'exame': exame})

def exames_do_paciente(request, id_paciente):
    response = "Você está olhando para os exames do paciente %s."
    return HttpResponse(response % id_paciente)

def add_exame(request):
    paciente_list = Paciente.objects.order_by('id_paciente')
    return render(request, 'gerenciamentoPEA/add_exame.html', {'paciente_list': paciente_list})

def add_paciente(request):
    return render(request, 'gerenciamentoPEA/add_paciente.html', {})

def save_paciente(request):
    try:#mudar aqui para nao aceitar id que ja existe
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

def save_exame(request):
    try:#mudar aqui para nao aceitar id que ja existe
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