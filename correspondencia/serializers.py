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

    #contacto = ContactoSerializer(many=False, read_only=True, required=False) Trae todo el array
    documentos = DocumentoSerializer(many=True, read_only=True, required=False)
    nombre_contacto = serializers.CharField(source='contacto.nombre_contacto', read_only=True) #Solo el nombre del contacto
    apellido_paterno_contacto = serializers.CharField(source='contacto.apellido_pat_contacto', read_only=True) #Solo el apellido del contacto
    apellido_materno_contacto = serializers.CharField(source='contacto.apellido_mat_contacto', read_only=True) #Solo el apellido del contacto
    cargo = serializers.CharField(source='contacto.cargo', read_only=True) #Solo el cargo del contacto
    titulo_profesional = serializers.CharField(source='contacto.titulo_profesional', read_only=True) #Solo el cargo del contacto
    nombre_completo = serializers.CharField(source='contacto.nombre_completo', read_only=True) #Solo el nombre completo del contacto
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
                'nombre_completo',
                'nombre_contacto',
                'apellido_paterno_contacto',
                'apellido_materno_contacto',
                'cargo',
                'titulo_profesional',

                


                #'usuario', #Usuario que crea la correspondencia
                
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