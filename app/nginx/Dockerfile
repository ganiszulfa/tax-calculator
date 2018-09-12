FROM nginx:1.13
RUN mkdir /var/www/theapp -p
RUN apt-get update
RUN apt-get install -y certbot 

RUN rm /etc/nginx/nginx.conf
ADD ./nginx.conf /etc/nginx/
ADD ./theapp_dev.conf /etc/nginx/conf.d/
#ADD ./theapp.conf /etc/nginx/conf.d/

