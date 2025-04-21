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
    class Meta:
        model = Contacto
        fields = [
            'id_contacto',
            'nombre_contacto',
            'apellido_pat_contacto',
            'apellido_mat_contacto',
            'cargo',
            'telefono',
            'email',
            'institucion',
        ]