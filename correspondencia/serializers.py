from .models import Correspondencia, DocEntrante, DocSaliente, DocInterno
from rest_framework import serializers
from documento.models import Documento
from documento.serializers import DocumentoSerializer
from contacto.serializers import ContactoSerializer 


class CorrespondenciaListSerializer(serializers.ModelSerializer): #Menos campos o solo los que se necesiten
   
   #Se obtiene el id del docuemento
   #documentos = serializers.PrimaryKeyRelatedField(many=True, queryset=Documento.objects.all())
   

   #se muestra el array de documentos, tener en cuenta el many=True
   #documentos = DocumentoSerializer(many=True, read_only=True, required=False)

    contacto = ContactoSerializer(many=False, read_only=True, required=False)
    documentos = DocumentoSerializer(many=True, read_only=True, required=False)
    class Meta: 
            model = Correspondencia
            fields = [
                'id_correspondencia',
                'fecha_registro',
                'referencia',
                'paginas',
                'prioridad',
                'estado',
                'documentos',
                'contacto',
                
            ]
        
class CorrespondenciaDetailSerializer(serializers.ModelSerializer): #Mas datos
    documentos = DocumentoSerializer(many=True, read_only=True, required=False)
    contacto = ContactoSerializer(many=False, read_only=True, required=False)
    class Meta: 
        model = Correspondencia
        fields = [
            'id_correspondencia',
            'fecha_registro',
            'referencia',
            'descripcion',
            'paginas',
            'prioridad',
            'estado',
            'comentario', 
            'documentos',
            'contacto',
        ]


#ENTRANTES
class DocEntranteSerializer(serializers.ModelSerializer):

    #Para ver los datos y no solo el id
    correspondencia = CorrespondenciaDetailSerializer()
    class Meta: 
        model = DocEntrante
        fields = [
            'id_doc_entrante',
            'nro_registro',
            'fecha_recepcion',
            'fecha_respuesta', 
            'correspondencia',
        ]
        read_only_fields = ['id_doc_entrante']
        
class DocSalienteSerializer(serializers.Serializer):
    class Meta:
        model = DocSaliente
        fields = '__all__'
        
class DocInternoSerializer(serializers.Serializer):
    class Meta:
        model = DocInterno
        fields = '__all__'