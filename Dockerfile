FROM python:3
MAINTAINER Daniel Jones <tortxof@gmail.com>

COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

COPY album_info.py /app/

ENTRYPOINT ["python3", "album_info.py"]
