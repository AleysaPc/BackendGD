from .mixins import PaginacionYAllDataMixin
from .serializers import CorrespondenciaSerializer, DocEntranteSerializer, DocSalienteSerializer, DocInternoSerializer
from rest_framework import viewsets
from .models import Correspondencia, DocEntrante, DocSaliente, DocInterno
# Create your views here.
class CorrespondenciaView(PaginacionYAllDataMixin, viewsets.ModelViewSet):
    serializer_class = CorrespondenciaSerializer
    queryset = Correspondencia.objects.all().order_by('id_correspondencia')
class DocEntranteView(PaginacionYAllDataMixin, viewsets.ModelViewSet):
    serializer_class = DocEntranteSerializer
    queryset = DocEntrante.objects.all().order_by('id_doc_entrante')

class DocSalienteView(PaginacionYAllDataMixin, viewsets.ModelViewSet):
    serializer_class = DocSalienteSerializer
    queryset = DocSaliente.objects.all().order_by('id_doc_saliente')

class DocInternoView(PaginacionYAllDataMixin, viewsets.ModelViewSet):
    serializer_class = DocInternoSerializer
    queryset = DocInterno.objects.all().order_by('id_doc_interno')
