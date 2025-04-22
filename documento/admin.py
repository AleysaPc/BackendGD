from django.contrib import admin
from .models import Documento, TipoDocumento, TipoDocumentoInterno
# Register your models here.
admin.site.register(Documento)
admin.site.register(TipoDocumento)
admin.site.register(TipoDocumentoInterno)