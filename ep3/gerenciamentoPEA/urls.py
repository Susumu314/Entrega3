from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pacientes/', views.pacientes, name='pacientes'),
    path('pacientes/<int:id_paciente>/', views.paciente_detail, name='p_detail'),
    path('pacientes/<int:id_paciente>/exames/', views.exames_do_paciente, name='exames_p'),
    # ex: /polls/5/vote/
    path('pacientes/<int:id_paciente>/adiciona_exame/', views.faz_exame, name='add_exame'),

]