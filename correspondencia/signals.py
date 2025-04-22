from django.db.models.signals import post_save 
from django.dispatch import receiver
from django.core.mail import EmailMessage
from django.conf import settings
from .models import DocEntrante, DocSaliente
import os

# Función para construir el mensaje del correo
def construir_mensaje(nro_registro, referencia, remitente, fecha_respuesta_formateada):
    if remitente:
        nombre_remitente = f"{remitente.nombre_contacto} {remitente.apellido_pat_contacto} {remitente.apellido_mat_contacto}"
        cargo_remitente = remitente.cargo
        empresa_remitente = remitente.institucion.razon_social if remitente.institucion else 'No especificado'
    else:
        nombre_remitente = 'No especificado'
        cargo_remitente = 'No especificado'
        empresa_remitente = 'No especificado'

    mensaje = f'Se ha registrado un nuevo documento con los siguientes detalles:\n\n'
    mensaje += f'Número de registro: {nro_registro}\n'
    mensaje += f'Referencia: {referencia}\n'
    mensaje += f'Remitente: {nombre_remitente}\n'
    mensaje += f'Cargo: {cargo_remitente}\n'
    mensaje += f'Empresa: {empresa_remitente}\n'
    mensaje += f'Fecha límite de respuesta: {fecha_respuesta_formateada or "No especificada"}\n'
    
    return mensaje

# Función para enviar el correo con adjunto
def enviar_correo(asunto, mensaje, archivo=None):
    destinatarios = ['isabella172813@gmail.com']
    email = EmailMessage(
        asunto,
        mensaje,
        'isatest172813@gmail.com',  # Remitente
        destinatarios,  # Lista de destinatarios
    )
    
    if archivo:
        email.attach_file(archivo.path)
    
    try:
        email.send(fail_silently=False)
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

# Para el envío de correo en documentos entrantes
@receiver(post_save, sender=DocEntrante)
def enviar_notificacion_correo(sender, instance, created, **kwargs):
    nro_registro = instance.nro_registro
    referencia = instance.correspondencia.referencia

    if created:  # Solo si se crea un nuevo documento
        print("Documento creado")

    fecha_respuesta_formateada = instance.fecha_respuesta.strftime('%d/%m/%Y %H:%M') if instance.fecha_respuesta else None
    mensaje = construir_mensaje(nro_registro, referencia, instance.correspondencia.contacto, fecha_respuesta_formateada)
    
    # Para adjuntar el documento
    documento = instance.correspondencia.documentos.first()
    if documento:
        enviar_correo(f'Nuevo documento registrado: {nro_registro}', mensaje, documento.archivo)
    else:
        enviar_correo(f'Nuevo documento registrado: {nro_registro}', mensaje)

# Para el envío de correo en documentos salientes
@receiver(post_save, sender=DocSaliente)
def enviar_notificacion_correo(sender, instance, created, **kwargs):
    if instance.correspondencia.estado == "en_revision":  # Solo enviar si el estado es "en_revision"
        cite = instance.cite
        referencia = instance.correspondencia.referencia
        destinatario = instance.correspondencia.contacto
        estado = instance.correspondencia.estado

        mensaje = f'Se ha elaborado un nuevo documento con los siguientes detalles:\n\n'
        mensaje += f'Nro. CITE: {cite}\n'
        mensaje += f'Referencia: {referencia}\n'
        mensaje += f'Destinatario: {destinatario.nombre_contacto} {destinatario.apellido_pat_contacto} {destinatario.apellido_mat_contacto}\n'
        mensaje += f'Cargo: {destinatario.cargo}\n'
        mensaje += f'Empresa: {destinatario.institucion.razon_social if destinatario.institucion else "No especificado"}\n'
        mensaje += f'Estado: {estado}\n'

        archivo = None
        if instance.archivo_word:
            ruta_documento = os.path.join(settings.MEDIA_ROOT, instance.archivo_word.name)
            if os.path.exists(ruta_documento):
                archivo = instance.archivo_word  # Usamos el archivo directamente si existe

        enviar_correo(f'Nuevo documento elaborado: {cite}', mensaje, archivo)
