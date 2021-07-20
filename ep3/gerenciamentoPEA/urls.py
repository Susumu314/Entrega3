from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('pacientes/', views.pacientes, name='pacientes'),
    path('pacientes/add_paciente/', views.add_paciente, name='add_paciente'),
    path('pacientes/save_paciente/', views.save_paciente, name='save_paciente'),
    path('pacientes/<int:id_paciente>/change_paciente', views.change_paciente, name='change_paciente'),
    path('pacientes/<int:id_paciente>/delete_paciente', views.delete_paciente, name='delete_paciente'),
    path('pacientes/<int:id_paciente>/', views.paciente_detail, name='p_detalhes'),
    path('pacientes/<int:id_paciente>/exames/', views.exames_do_paciente, name='p_exames'),

    path('exames/', views.exames, name='exames'),
    path('exames/<int:id_exame>/', views.exame_detail, name='e_detalhes'),
    path('exames/adiciona_exame/', views.add_exame, name='add_exame'),
    path('exames/save_exame/', views.save_exame, name='save_exame'),
    path('exames/<int:id_exame>/change_exame', views.change_exame, name='change_exame'),
    path('exames/<int:id_exame>/delete_exame', views.delete_exame, name='delete_exame'),

    path('amostras/', views.amostras, name='amostras'),
    path('amostras/add_amostra/', views.add_amostra, name='add_amostra'),
    path('amostras/save_amostra/', views.save_amostra, name='save_amostra'),
    path('amostras/<int:id_amostra>/change_amostra', views.change_amostra, name='change_amostra'),
    path('amostras/<int:id_amostra>/delete_amostra', views.delete_amostra, name='delete_amostra'),
    path('amostras/<int:id_amostra>/', views.amostra_detail, name='a_detalhes'),

    path('agregadoPEAs/', views.agregadoPEAs, name='agregadoPEAs'),
    path('agregadoPEAs/<int:id_agregadoPEA>/', views.agregadoPEA_detail, name='ag_detalhes'),
    path('agregadoPEAs/adiciona_agregadoPEA/', views.add_agregadoPEA, name='add_agregadoPEA'),
    path('agregadoPEAs/save_agregadoPEA/', views.save_agregadoPEA, name='save_agregadoPEA'),
    path('agregadoPEAs/<int:id_agregadoPEA>/change_agregadoPEA', views.change_agregadoPEA, name='change_agregadoPEA'),
    path('agregadoPEAs/<int:id_agregadoPEA>/delete_agregadoPEA', views.delete_agregadoPEA, name='delete_agregadoPEA'),
]