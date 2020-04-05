from django.contrib import admin
from donatario.models import Grantee
# Register your models here.

class GranteeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'whatsapp', 'email', 'estado', 'cidade', 'atendido')
    search_fields = ('nome', 'whatsapp', 'email', 'estado', 'cidade')
    list_filter = ('atendido',)



admin.site.register(Grantee, GranteeAdmin)