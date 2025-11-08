FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app
COPY app/          ./app/
COPY config.py     .
COPY specs/        ./specs/


# Initialize the database (if needed)
RUN python -c "from app import create_app, db; app = create_app(); with app.app_context(): db.create_all()"


EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
