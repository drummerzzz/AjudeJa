from django.contrib import admin
from doacao.models import Donation

# Register your models here.
class DonationAdmin(admin.ModelAdmin):
    list_display = ('doador', 'donatario','avisado')
    search_fields = ('doador__nome', 'donatario__nome', 'email')
    list_filter = ('avisado',)


admin.site.register(Donation, DonationAdmin)