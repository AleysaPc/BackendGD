from django.contrib import admin
from .models import Correspondencia, DocEntrante, DocSaliente, DocInterno
from documento.models import Documento

admin.site.register(Correspondencia)
admin.site.register(DocEntrante)
admin.site.register(DocSaliente)
admin.site.register(DocInterno)
