from django.contrib import admin
from doador.models import Donor

class DonornAdmin(admin.ModelAdmin):
    list_display = ('nome', 'whatsapp')
    search_fields = ('nome', 'whatsapp',)

admin.site.register(Donor, DonornAdmin)