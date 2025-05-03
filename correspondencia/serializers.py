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

    #contacto = ContactoSerializer(many=False, read_only=True, required=False) 
    documentos = DocumentoSerializer(many=True, read_only=True, required=False)
    
    
    class Meta: 
            model = Correspondencia
            fields = [
                'id_correspondencia',
                'tipo',
                'descripcion', #Descripción esta si aparece en la creación del frontend
                'fecha_registro',
                'referencia',
                'paginas',
                'prioridad',
                'estado',
                'documentos',
                'contacto', #Unicamente necesitamos el ID para el registro en el frontend
                'usuario', #Usuario que crea la correspondencia
                'comentario',
              
              

                


                #'usuario', #Usuario que crea la correspondencia
                
            ]
        
class CorrespondenciaDetailSerializer(serializers.ModelSerializer): #Para obetner uno solo por el ID
    documentos = DocumentoSerializer(many=True, read_only=True, required=False)
    #contacto = ContactoSerializer(many=False, read_only=True, required=False)
    class Meta: 
        model = Correspondencia
        fields = [
            'id_correspondencia',
            'tipo',
            'fecha_registro',
            'comentario',
            'referencia',
            'descripcion',
            'paginas',
            'prioridad',
            'estado',
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