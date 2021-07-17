from django.contrib import admin

from .models import Paciente
from .models import Amostra
from .models import Exame
from .models import Paciente_exame_amostra

admin.site.register(Paciente)
admin.site.register(Amostra)
admin.site.register(Exame)
admin.site.register(Paciente_exame_amostra)
# Register your models here.
