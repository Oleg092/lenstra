FROM nginx:latest

# setup nginx
ADD ./nginx.conf /etc/nginx/nginx.conf

# add project files
ADD . /usr/share/nginx/html/

# Adding read permissions to custom index.html
RUN chmod +r /usr/share/nginx/html/index.html

CMD ["nginx", "-g", "daemon off;"]