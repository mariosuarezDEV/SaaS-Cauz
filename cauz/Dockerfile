FROM node:22

# Establecer el directorio de trabajo
WORKDIR /app

# Pasar los requerimientos de la aplicación
COPY package*.json ./

# Instalar las dependencias
RUN npm install

# Copiar el código de la aplicación
COPY . .

# Exponer el puerto 4003
EXPOSE 4003

# Iniciar la aplicación
CMD ["npm", "run", "dev"]