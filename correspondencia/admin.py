from django.contrib import admin
from .models import Correspondencia, DocEntrante, DocSaliente, DocInterno
from documento.models import Documento

class DocumentoInline(admin.TabularInline):  # O usa StackedInline si prefieres un formato más vertical
    model = Documento
    extra = 1  # Número de formularios vacíos para agregar documentos
    fields = ['archivo','nombre_documento', 'tipo_documento']  # Campos a mostrar del Documento

class CorrespondenciaAdmin(admin.ModelAdmin):
    list_display = ['id_correspondencia', 'fecha_registro', 'referencia']  # Campos para listar en la vista de la lista
    inlines = [DocumentoInline]  # Agregamos el Inline para mostrar documentos

# Registramos los modelos en el admin
admin.site.register(Correspondencia, CorrespondenciaAdmin)
admin.site.register(DocEntrante)
admin.site.register(DocSaliente)
admin.site.register(DocInterno)
