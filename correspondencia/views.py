from .serializers import CorrespondenciaListSerializer, CorrespondenciaDetailSerializer, DocEntranteSerializer, DocSalienteSerializer, DocInternoSerializer
from rest_framework import viewsets
from .models import Correspondencia, DocEntrante, DocSaliente, DocInterno
from gestion_documental.mixins import PaginacionYAllDataMixin
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import generar_documento_word
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class CorrespondenciaView(PaginacionYAllDataMixin, viewsets.ModelViewSet):
    queryset = Correspondencia.objects.all().order_by('id_correspondencia')

    def get_serializer_class(self):
        if self.action == 'list':
            return CorrespondenciaListSerializer
        elif self.action == 'retrieve':
            return CorrespondenciaDetailSerializer
        return CorrespondenciaListSerializer
    
    #Para las rutas hacias recibido y enviado
    @action(detail=False, methods=['get'])
    def recibidos(self, request):
        queryset = self.get_queryset().filter(tipo='recibido').order_by('id_correspondencia')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def enviados(self, request):
        queryset = self.get_queryset().filter(tipo='enviado').order_by('id_correspondencia')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class DocEntranteView(PaginacionYAllDataMixin, viewsets.ModelViewSet):
    serializer_class = DocEntranteSerializer
    queryset = DocEntrante.objects.all().order_by('id_doc_entrante')

class DocSalienteView(PaginacionYAllDataMixin, viewsets.ModelViewSet):
    serializer_class = DocSalienteSerializer
    queryset = DocSaliente.objects.all().order_by('id_doc_saliente')

class DocInternoView(PaginacionYAllDataMixin, viewsets.ModelViewSet):
    serializer_class = DocInternoSerializer
    queryset = DocInterno.objects.all().order_by('id_doc_interno')

@csrf_exempt
def generar_documento(request, id):
    if request.method == "POST":
        try:
            correspondencia = Correspondencia.objects.get(id=id)
            response = generar_documento_word(correspondencia)  # Llamar a la función
            return response  # Esto debería devolver un archivo
        except Correspondencia.DoesNotExist:
            return JsonResponse({"error": "Correspondencia no encontrada"}, status=404)
    return JsonResponse({"error": "Método no permitido"}, status=405)