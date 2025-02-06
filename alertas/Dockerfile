FROM python:3.12-bullseye

WORKDIR /flask_services

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Run the application
EXPOSE 4001
CMD ["python", "app.py"]