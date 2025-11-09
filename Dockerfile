FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app
COPY app/          ./app/
COPY config.py     .
COPY specs/        ./specs/

COPY app.db        .

EXPOSE 5000

# ----------------------------------------------------------------
#  Production entrypoint – Gunicorn
# ----------------------------------------------------------------
# * `app:create_app()` is the Flask factory that returns the Flask instance.
# * `--bind 0.0.0.0:5000` makes the server reachable from outside the container.
# * `--workers $(nproc)` starts 2 × CPU cores + 1 workers (adjust as needed).
# * `--log-level info` gives a clean log; change to debug for more detail.
CMD ["gunicorn", "app:create_app()", \
     "--bind", "0.0.0.0:5000", \
     "--workers", "4", \
     "--log-level", "info"]
