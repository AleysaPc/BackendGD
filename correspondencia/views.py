from rest_framework.pagination import PageNumberPagination
from .serializers import CorrespondenciaSerializer, DocEntranteSerializer, DocSalienteSerializer, DocInternoSerializer
from rest_framework import viewsets
from .models import Correspondencia, DocEntrante, DocSaliente, DocInterno
# Create your views here.
class PaginacionPersonalizada(PageNumberPagination):
    page_size = 10  # Número predeterminado de elementos por página
    page_size_query_param = 'page_size'  # Permitir cambiar el tamaño de la página desde los parámetros de la consulta
    max_page_size = 100  # Tamaño máximo de página permitido

class CorrespondenciaView(viewsets.ModelViewSet):
    serializer_class = CorrespondenciaSerializer
    queryset = Correspondencia.objects.all().order_by('id_correspondencia')

    pagination_class = PaginacionPersonalizada

    def list(self, request, *args, **kwargs):
        all_data = request.query_params.get('all_data', 'false').lower() == 'true'  # Convierte a booleano correctamente

        if all_data:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)

        return super().list(request, *args, **kwargs)  # Usa la paginación normal
    
class DocEntranteView(viewsets.ModelViewSet):
    serializer_class = DocEntranteSerializer
    queryset = DocEntrante.objects.all().order_by('id_doc_entrante')

    pagination_class = PaginacionPersonalizada

    def list(self, request, *args, **kwargs):
        all_data = request.query_params.get('all_data', 'false').lower() == 'true'  # Convierte a booleano correctamente

        if all_data:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)

        return super().list(request, *args, **kwargs)  # Usa la paginación normal

class DocSalienteView(viewsets.ModelViewSet):
    serializer_class = DocSalienteSerializer
    queryset = DocSaliente.objects.all().order_by('id_doc_saliente')

    pagination_class = PaginacionPersonalizada

    def list(self, request, *args, **kwargs):
        all_data = request.query_params.get('all_data', 'false').lower() == 'true'  # Convierte a booleano correctamente

        if all_data:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)

        return super().list(request, *args, **kwargs)  # Usa la paginación normal

class DocInternoView(viewsets.ModelViewSet):
    serializer_class = DocInternoSerializer
    queryset = DocInterno.objects.all().order_by('id_doc_interno')

    pagination_class = PaginacionPersonalizada

    def list(self, request, *args, **kwargs):
        all_data = request.query_params.get('all_data', 'false').lower() == 'true'  # Convierte a booleano correctamente

        if all_data:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)

        return super().list(request, *args, **kwargs)  # Usa la paginación normal