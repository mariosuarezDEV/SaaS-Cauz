from django.db.models.signals import post_save, pre_save # Enviar señales después de guardar
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
    asunto=  f'¡Buenas noticias {postulante.nombre}! 🎉'
    mensaje= f"""
¡Buenas noticias! 🎉 Los cambios solicitados para el evento **{instancia.nombre_evento}** han sido procesados y actualizados con éxito.

Aquí te dejamos los detalles más recientes: 

---

🔹 **📌 Nombre del Evento:**  
*{instancia.nombre_evento}*

🔹 **📅 Fecha Tentativa:**  
*{instancia.fecha_tentativa}*

🔹 **🎶 Género Musical:**  
*{instancia.genero}*

🔹 **👥 Integrantes:**  
*{instancia.integrantes}*

🔹 **📂 Material Requerido:**  
*{instancia.meterial}*

---

Si necesitas hacer más ajustes o tienes alguna consulta, ¡no dudes en ponerte en contacto con nosotros! Estamos aquí para ayudarte. 🤝

Gracias por ser parte de **Foro CAUZ**, y ¡esperamos contar con tu participación! 🚀

Saludos cordiales,  
**El equipo de Foro CAUZ**  

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
        

def change_status(postulante, instancia):
    asunto=  f'¡La solicitud de tu evento ha sido actualizada! 🎉'
    mensaje= f'El estado de la solicitud de tu evento **{instancia.nombre_evento}** ha sido actualizado a **{instancia.estado}**.'
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

# Creamos un diccionario para almacenar las instancias anteriores
previous_instances = {}

@receiver(pre_save, sender=ModelSolicitudEventos)
def save_previous_instance(sender, instance, **kwargs):
    # Guardamos la instancia anterior antes de que se guarde la nueva
    try:
        previous_instance = sender.objects.get(id=instance.id)
        previous_instances[instance.id] = previous_instance
    except sender.DoesNotExist:
        # Si la instancia no existe, es porque es nueva, por lo que no hace falta guardar la versión anterior
        pass

@receiver(post_save, sender=ModelSolicitudEventos) # Recibir señales después de guardar
def nueva_solicitud(sender, instance, created, **kwargs): # Definir la función que manejará las señales
    if created: # Si se ha creado
        postulante = ModelPostulante.objects.get(id=instance.postulante.id) # Obtener el postulante que ha hecho la solicitud
        # Informacion de la solicitud
        use_send_email_service_for_new_query(postulante.correo, instance) # Enviar un correo de recibido al postulante
    else: # Si no
        postulante = ModelPostulante.objects.get(id=instance.postulante.id)
        # Verificamos si la instancia anterior está almacenada
        previous_instance = previous_instances.get(instance.id)

        if previous_instance:  # Si existe la instancia anterior
            if previous_instance.estado != instance.estado:  # Si el estado ha cambiado
                change_status(postulante, instance)  # Ejecutar la función para cambio de estado
            else:
                enviar_correo_actualizacion(postulante, instance)  # Si no, es otra actualización
        else:
            # En caso de que no haya instancia anterior (por ejemplo, si es la primera vez que se guarda)
            enviar_correo_actualizacion(postulante, instance)
        