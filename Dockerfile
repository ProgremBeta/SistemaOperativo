FROM python:3.12-slim

WORKDIR /Sistema

COPY . /Sistema

RUN pip3 --no-cache-dir install -r Requerimientos.txt

CMD ["python","index.py"]