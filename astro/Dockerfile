FROM node:22.13.1-bullseye

# Install basic development tools
RUN apt update && apt install -y less man-db sudo

# Set `DEVCONTAINER` environment variable to help with orientation
ENV DEVCONTAINER=true

WORKDIR /app

# Copy the local package files to the container's workspace
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the local source files to the container's workspace
COPY . .

# Expose the port the app runs on
EXPOSE 4003

# Serve the app
CMD ["npm", "run", "dev"]

