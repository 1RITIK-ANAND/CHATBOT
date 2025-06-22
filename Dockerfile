# Use full Python 3.11 base image (not slim)
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy dependency list and install
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy remaining app code
COPY . /app/

# Make Gradio public (inside container)
ENV GRADIO_SERVER_NAME=0.0.0.0

# Expose port 7860
EXPOSE 7860

# Start Gradio app
CMD ["python", "main.py"]
