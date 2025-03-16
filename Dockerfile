FROM python 

WORKDIR /app
COPY . /app
CMD python rab.py