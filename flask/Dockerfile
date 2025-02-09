FROM python:3.12-bullseye

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source code
COPY . .

# Run the application
EXPOSE 4001
CMD ["python", "app.py"]