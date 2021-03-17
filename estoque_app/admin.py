from django.contrib import admin
from estoque_app.models import Estoque

class Estoque(admin.ModelAdmin):
    list_display = ('id', 'nome', 'valor')
    list_display_links = ('nome','valor')
    search_fields = ('nome',)

    admin.site.register(Estoque)
