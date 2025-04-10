
from rest_framework import serializers
from .models import Documento, TipoDocumento

class DocumentoSerializer(serializers.ModelSerializer):

    archivo = serializers.FileField(required=True)
    
    class Meta:
        model = Documento
        fields = ['id_documento', 'archivo', 'nombre_documento']

class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = '__all__'