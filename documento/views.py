from rest_framework import viewsets
from .serializers import TipoDocumentoSerializer, DocumentoSerializer
from .models import TipoDocumento, Documento
# Create your views here.
# Tambien va la paginacion

class TipoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer