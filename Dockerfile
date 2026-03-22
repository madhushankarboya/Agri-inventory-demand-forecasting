FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ✅ Correct JSON format + PORT support
CMD ["sh", "-c", "gunicorn run:app --bind 0.0.0.0:$PORT"]
