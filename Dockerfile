FROM python:3.11.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

# Clean install with no cache to avoid leftover versions
RUN pip install --upgrade pip && \
    pip uninstall -y openai || true && \
    pip install openai==0.28.1 && \
    pip install -r requirements.txt

COPY . /app/

ENV GRADIO_SERVER_NAME=0.0.0.0

EXPOSE 7860

CMD ["python", "main.py"]
