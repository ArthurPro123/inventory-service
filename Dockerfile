FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app
COPY app/          ./app/
COPY config.py     .
COPY specs/        ./specs/


EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
