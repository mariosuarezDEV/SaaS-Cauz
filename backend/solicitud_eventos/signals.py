from django.db.models.signals import post_save # Enviar señales después de guardar
from django.dispatch import receiver # Recibir señales

from .models import ModelSolicitudEventos # Importar el modelo SolicitudEvento
from postulantes.models import ModelPostulante # Importar el modelo Postulante (nos servirá para obtener el correo del postulante)

# Correo de recibido (servicio creado en flask)
import requests # Requests para hacer peticiones HTTP

servidor = 'flask'
puerto = 4001
endpoint = f'http://{servidor}:{puerto}/send_email'

def use_send_email_service_for_new_query(email, detalles):
    """
    Enviar un correo de recibido al usuario que ha hecho una solicitud de evento
    """
    # Elementos que necesita el endpoint
    asunto = "¡Te damos la bienvenida a Foro Cauz!" # Asunto del correo
    mensaje = f"""
# 🎉 ¡Nos emociona saber que quieres ser parte de Foro Cauz! 🎉


¡Tu solicitud para el evento ha llegado a nuestras manos y estamos ansiosos por verlo en acción! 😍


Aquí te dejamos los detalles de tu evento:


🔹 **Nombre del evento**: {detalles.nombre_evento}


🔹 **Fecha tentativa**: {detalles.fecha_tentativa}


🔹 **Género**: {detalles.genero}


🔹 **Integrantes**: {detalles.integrantes}


🔹 **Material**: {detalles.meterial}


Si necesitas realizar algún cambio o tienes alguna duda, no dudes en ponerte en contacto con nosotros. ¡Estamos aquí para ayudarte! 😊


Gracias por confiar en nosotros, ¡esto va a ser increíble! 🚀


Con mucho entusiasmo,
**Foro Cauz**
"""

    try:
        print(f'Enviando correo a {email}')
        # Hacer la petición
        response = requests.post(endpoint, json={
            'email': email,
            'asunto': asunto,
            'mensaje': mensaje,
        })
        print(response.json())
    except Exception as e:
        print('No se puede imprimir el correo')   
        
def enviar_correo_actualizacion (postulante, instancia):
    asunto=  "¡Actualización Exitosa del Evento! 🎉"
    mensaje= f"""
    **Estimado/a {postulante.nombre} {postulante.apellido_paterno} {postulante.apellido_materno}**,
    
    
Les informamos que los cambios en el evento [nombre del evento] se han realizado exitosamente.

Detalles actualizados:


🔹 📌 **Nombre del evento: ** {instancia.nombre_evento}


🔹 📅 **Fecha tentativa: ** {instancia.fecha_tentativa}


🔹 🎶 **Género: ** {instancia.genero}


🔹 👥 **Integrantes: ** {instancia.integrantes}


🔹 📂 **Material: ** {instancia.meterial}


Por favor, no duden en contactarnos si tienen algun otro cambio.


¡Gracias por su atención y esperamos contar con su participación!


Saludos cordiales,


**Foro CAUZ**
    """
    try:
        print(f'Enviando correo a {postulante.correo}')
        # Hacer la petición
        response = requests.post(endpoint, json={
            'email': postulante.correo,
            'asunto': asunto,
            'mensaje': mensaje,
        })
        print(response.json())
    except Exception as e:
        print('No se puede imprimir el correo')  

@receiver(post_save, sender=ModelSolicitudEventos) # Recibir señales después de guardar
def nueva_solicitud(sender, instance, created, **kwargs): # Definir la función que manejará las señales
    if created: # Si se ha creado
        #postulante = ModelPostulante.objects.get(id=instance.postulante) # Obtener el postulante que ha hecho la solicitud
        #use_send_email_service_for_new_query(postulante.correo) # Enviar un correo de recibido al postulante
        #print(f"Nuevo objeto de {sender} ha sido guardado: {instance.postulante.id}") # Imprimir en consola
        postulante = ModelPostulante.objects.get(id=instance.postulante.id) # Obtener el postulante que ha hecho la solicitud
        # Informacion de la solicitud
        use_send_email_service_for_new_query(postulante.correo, instance) # Enviar un correo de recibido al postulante
    else: # Si no
        postulante = ModelPostulante.objects.get(id=instance.postulante.id)
        enviar_correo_actualizacion(postulante, instance)
        #print('Se ha modificado una solicitud de evento') # Imprimir en consola