FROM  python:3.11-slim-bullseye
WORKDIR /app
ENV PYTHONUNBUFFERED 1
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]