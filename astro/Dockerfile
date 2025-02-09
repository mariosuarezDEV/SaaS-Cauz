FROM node:22.13.1-bullseye

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 4003

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "4003"]