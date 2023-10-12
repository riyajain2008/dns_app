FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install Flask
RUN pip install pytz
RUN pip install requests

EXPOSE 9090

CMD ["python", "FS_Server.py"]
