FROM python:3.12-bullseye

WORKDIR /app/alertas

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Run the application
EXPOSE 8080
CMD ["python", "app.py"]