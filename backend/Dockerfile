FROM ubuntu

RUN apt-get update && apt-get install -y python3-pip python3.5

RUN pip3 install bottle && pip3 install gunicorn && pip3 install gevent \
&& pip3 install -U "python-dotenv[cli]"

ADD . /app
WORKDIR /app

#RUN cp env.example .env

EXPOSE 8080

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

CMD ["gunicorn","-b","0.0.0.0:8080","-w","3","-k","gevent","--log-file","-","--log-level","debug","--access-logfile","-","app:app"]
