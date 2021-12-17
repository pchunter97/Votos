from django.contrib import admin

# Register your models here select.
from .models import t_padron_electoral, t_datos_eleccion, t_partido, t_voto, t_escrutinio
# Register your models here.
admin.site.register(t_padron_electoral)
admin.site.register(t_datos_eleccion)
admin.site.register(t_partido)
admin.site.register(t_voto)
admin.site.register(t_escrutinio)

