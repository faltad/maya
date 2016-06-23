FROM ubuntu:latest

MAINTAINER Alex Raileanu "alexraileanu@me.com"

RUN apt-get update

RUN apt-get install -y  python \
                        python-dev \
                        python-distribute \
                        python-pip \
                        apache2 \ 
                        apache2-utils \
                        libapache2-mod-wsgi \ 
                        libmysqlclient-dev \
                        vim \
                        mysql-client

ADD . /var/www/html/maya
RUN mkdir /var/www/html/maya/logs

RUN pip install -r /var/www/html/maya/requirements.txt

RUN mv /var/www/html/maya/config/prod.cfg /var/www/html/maya/current.cfg

RUN cp /var/www/html/maya/deploy/apache/maya.conf /etc/apache2/sites-available/maya.conf
RUN a2ensite maya.conf
RUN a2dissite 000-default.conf

WORKDIR /var/www/html/maya

EXPOSE 80

ENTRYPOINT /usr/sbin/apache2ctl -D FOREGROUND