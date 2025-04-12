from .serializers import CorrespondenciaListSerializer, CorrespondenciaDetailSerializer, DocEntranteSerializer, DocSalienteSerializer, DocInternoSerializer
from rest_framework import viewsets
from .models import Correspondencia, DocEntrante, DocSaliente, DocInterno
from gestion_documental.mixins import PaginacionYAllDataMixin

# Create your views here.
class CorrespondenciaView(PaginacionYAllDataMixin, viewsets.ModelViewSet):
    queryset = Correspondencia.objects.all().order_by('id_correspondencia')

    def get_serializer_class(self):
        if self.action == 'list':
            return CorrespondenciaListSerializer
        elif self.action == 'retrieve':
            return CorrespondenciaDetailSerializer
        return CorrespondenciaListSerializer
    
class DocEntranteView(PaginacionYAllDataMixin, viewsets.ModelViewSet):
    serializer_class = DocEntranteSerializer
    queryset = DocEntrante.objects.all().order_by('id_doc_entrante')

class DocSalienteView(PaginacionYAllDataMixin, viewsets.ModelViewSet):
    serializer_class = DocSalienteSerializer
    queryset = DocSaliente.objects.all().order_by('id_doc_saliente')

class DocInternoView(PaginacionYAllDataMixin, viewsets.ModelViewSet):
    serializer_class = DocInternoSerializer
    queryset = DocInterno.objects.all().order_by('id_doc_interno')

