from flask import Flask, request, jsonify

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Flask services!</h1>'

@app.route('/ping')
def ping_pong():
    return jsonify({
        'message': 'pong!'
    })
    
# Enviar un correo electronico
@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.get_json()
    
    email = data['email']
    asunto = data['asunto']
    mensaje_api = data['mensaje']
    # Validar que los datos esten completos
    if not email or not asunto or not mensaje_api:
        return jsonify({
            'message': 'Datos incompletos'
        }), 400
        
    # Enviar correo electronico
    # Datos del correo
    remitente = "lmcervantessuarez@gmail.com"
    destinatario = email
    contraseña = "htdi zwjv hbkv uqqr"  # Asegúrate de utilizar una contraseña segura

    # Crear el mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto

    # Cuerpo del mensaje
    cuerpo = mensaje_api
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Establecer la conexión con el servidor SMTP de Gmail
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()  # Iniciar la conexión TLS (cifrado)
        servidor.login(remitente, contraseña)  # Iniciar sesión en el servidor

        # Enviar el correo
        texto = mensaje.as_string()
        servidor.sendmail(remitente, destinatario, texto)
        print("Correo enviado exitosamente!")
        return jsonify({
            'message': 'Correo enviado exitosamente!'
        }), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({
            'message': 'Error al enviar el correo'
        }), 500

    finally:
        servidor.quit()  # Cerrar la conexión con el servidor
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4001)
