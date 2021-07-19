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
    path('exames/adiciona_exame/', views.add_exame, name='add_exame'),
    path('exames/save_exame/', views.save_exame, name='save_exame'),
]