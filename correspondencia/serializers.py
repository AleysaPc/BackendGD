from .models import Correspondencia, DocEntrante, DocSaliente, DocInterno
from rest_framework import serializers
from documento.models import Documento
from documento.serializers import DocumentoSerializer

class CorrespondenciaSerializer(serializers.ModelSerializer):
    documentos = DocumentoSerializer(many=True, read_only=True)  # Para crear documentos al mismo tiempo
    
    class Meta:
        model = Correspondencia
        fields = ['id_correspondencia','fecha_registro', 'referencia', 'descripcion', 'paginas', 'prioridad', 'estado', 'comentario', 'documentos']

class DocEntranteSerializer(serializers.ModelSerializer):
    documentos = DocumentoSerializer(many=True, read_only=True)
    correspondencia = CorrespondenciaSerializer(read_only=True)  # Solo lectura para evitar problemas de creación

    class Meta: 
        model = DocEntrante
        fields = ['id_doc_entrante', 'nro_registro', 'fecha_recepcion', 'fecha_respuesta', 'documentos', 'correspondencia']


class DocSalienteSerializer(serializers.Serializer):
    class Meta:
        model = DocSaliente
        fields = '__all__'
        
class DocInternoSerializer(serializers.Serializer):
    class Meta:
        model = DocInterno
        fields = '__all__'