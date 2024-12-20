FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# EXPOSE 443
EXPOSE 80

CMD ["python", "serve_model.py"]