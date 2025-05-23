FROM python:3.12-slim

WORKDIR /app

# Copy all files to preserve structure
COPY . .

RUN pip install --no-cache-dir -r app/requirements.txt \
    && pip install pytest

EXPOSE 8000

ENV PYTHONPATH=/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
