FROM python:3.12-bullseye

WORKDIR /app

RUN apt update && apt-get -y install default-libmysqlclient-dev build-essential pkg-config

# Instalar depencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copiar codigo fuente
COPY . . 

#Correr aplicacion
EXPOSE 4000
CMD ["python", "manage.py", "runserver", "0.0.0.0:4000"]
