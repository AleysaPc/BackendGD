from django.db import models
from django.db import transaction
from django.utils.timezone import now

# Create your models here.
class Correspondencia(models.Model):
    TIPO_CHOICES_ESTADO = [('borrador', 'Borrador'),('en_revision', 'En revisión'), ('aprobado', 'Aprobado'), ('rechazado', 'Rechazado')]
    TIPO_CHOICES_PRIORIDAD = [('alta', 'Alta'), ('media', 'Media'), ('baja', 'Baja')]
    id_correspondencia = models.AutoField(primary_key=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    referencia = models.CharField(max_length=255)
    descripcion = models.TextField()
    paginas = models.IntegerField(null=False, blank=False)
    prioridad = models.CharField(max_length=20, choices=TIPO_CHOICES_PRIORIDAD)
    estado = models.CharField(max_length=20, choices=TIPO_CHOICES_ESTADO, default='en_revision')
    comentario = models.TextField(null=False, blank=False) 

    def __str__(self):
        return f"{self.referencia} "

class DocEntrante(models.Model):
    id_doc_entrante = models.AutoField(primary_key=True)
    nro_registro = models.CharField(max_length=50, blank=True, null=True)
    fecha_recepcion = models.DateTimeField(blank=True, null=True)
    fecha_respuesta = models.DateTimeField(blank=True, null=True)
    correspondencia = models.ForeignKey(Correspondencia, on_delete=models.CASCADE, related_name='documentos_entrantes')
    def save(self, *args, **kwargs):
        if not self.nro_registro:
            with transaction.atomic():
                # Obtiene el último número de registro
                ultimo = DocEntrante.objects.order_by('-id_doc_entrante').first()
                nuevo_numero = (int(ultimo.nro_registro.split('-')[1]) + 1 if ultimo and ultimo.nro_registro else 1)
                self.nro_registro = f'Reg-{nuevo_numero:03}'
    
        super().save(*args, **kwargs)

class DocSaliente(models.Model):
    id_doc_saliente = models.AutoField(primary_key=True)
    cite = models.CharField(max_length=50, blank=True, null=True)
    fecha_envio = models.DateTimeField(blank=True, null=True)
    fecha_recepcion = models.DateTimeField(blank=True, null=True)
    fecha_seguimiento = models.DateTimeField(blank=True, null=True)
    archivo_word = models.FileField(upload_to='documentos_borrador/', blank=True, null=True)
    correspondencia = models.ForeignKey(Correspondencia, on_delete=models.CASCADE, related_name='documentos_salientes')

    def save(self, *args, **kwargs):
        if not self.cite:
            with transaction.atomic():
                # Obtiene el último cite registrado y lo incrementa
                ultimo = DocSaliente.objects.order_by('-id_doc_saliente').first()
                nuevo_cite = (int(ultimo.cite.split('-')[-1]) + 1 if ultimo and ultimo.cite else 1)
                self.cite = f'CITE:FTL-FTA/DLP/Nro.-{nuevo_cite:04}'

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cite}"

class DocInterno(models.Model):
    id_doc_interno = models.AutoField(primary_key=True)
    numero = models.PositiveIntegerField(editable=False)  # Número secuencial único
    gestion = models.PositiveIntegerField(default=now().year, editable=False)  # Año de gestión
    cite = models.CharField(max_length=100, unique=True, blank=True)  # Código único del documento
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    correspondencia = models.ForeignKey(Correspondencia, on_delete=models.CASCADE, related_name='documentos_internos')
    def __str__(self):
        return f"{self.numero}"
    