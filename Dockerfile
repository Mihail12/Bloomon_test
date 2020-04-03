FROM python:3.8.2-alpine
WORKDIR /data
VOLUME /data
ADD . /data
CMD [ "python", "./bouquet_maker.py" ]