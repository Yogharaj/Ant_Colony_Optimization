FROM python:3.9-slim

WORKDIR /app
COPY load.py /app

RUN pip install Flask requests 

EXPOSE 5003
CMD ["python", "load.py"]
