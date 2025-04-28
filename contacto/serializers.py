from .models import Contacto, Institucion
from rest_framework import serializers


class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = [
            'id_institucion',
            'razon_social',
            'direccion',
            'telefono',
            'fecha_fundación',
        ]

class ContactoSerializer(serializers.ModelSerializer):  
    institucion = InstitucionSerializer(read_only=True, required=False) #ojo con el many=True, ya que no se puede usar en este caso, ya que no es una lista de objetos, sino un solo objeto.
    nombre_completo = serializers.SerializerMethodField()
    
    class Meta:
        model = Contacto
        fields = [
            'id_contacto',
            'nombre_contacto',
            'titulo_profesional',
            'apellido_pat_contacto',
            'apellido_mat_contacto',
            'cargo',
            'telefono',
            'email',
            'institucion',
            'nombre_completo',
        ]
    def get_nombre_completo(self, obj):
        return f"{obj.nombre_contacto} {obj.apellido_pat_contacto} {obj.apellido_mat_contacto} - {obj.titulo_profesional} - {obj.institucion.razon_social}"