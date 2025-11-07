FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/          ./app/
COPY config.py     .
COPY openapi.json  .


# Document the port the container listens on:
EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
