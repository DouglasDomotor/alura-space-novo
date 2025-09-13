from django.contrib import admin

from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda','publicada')
    list_display_links = ('id', 'nome')
    list_filter = ('nome',)
    list_editable = ('publicada',)
    list_per_page = 10

admin.site.register(Fotografia, ListandoFotografias)
