from .models import Correspondencia, DocEntrante, DocSaliente, DocInterno
from rest_framework import serializers
from documento.models import Documento
from documento.serializers import DocumentoSerializer


class CorrespondenciaSerializer(serializers.ModelSerializer):
   
   #Se obtiene el id del docuemento
   #documentos = serializers.PrimaryKeyRelatedField(many=True, queryset=Documento.objects.all())
   

   #Smuestra el array de documentos, tener en cuenta el many=True
   documentos = DocumentoSerializer(many=True, read_only=True, required=False)
   class Meta: 
         model = Correspondencia
         fields = ['id_correspondencia','fecha_registro','referencia','descripcion','paginas','prioridad','estado','comentario','documentos']
    

#ENTRANTES
class DocEntranteSerializer(serializers.ModelSerializer):

    #Para ver los datos y no solo el id
    correspondencia = CorrespondenciaSerializer()
    class Meta: 
        model = DocEntrante
        fields = ['id','nro_registro','fecha_recepcion','fecha_respuesta', 'correspondencia']

class DocSalienteSerializer(serializers.Serializer):
    class Meta:
        model = DocSaliente
        fields = '__all__'
        
class DocInternoSerializer(serializers.Serializer):
    class Meta:
        model = DocInterno
        fields = '__all__'