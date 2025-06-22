FROM python:3.11.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy rest of the app
COPY . /app/

# Set Gradio public (important)
ENV GRADIO_SERVER_NAME=0.0.0.0

# Expose Gradio port
EXPOSE 7860

# Run the chatbot
CMD ["python", "main.py"]
