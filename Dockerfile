FROM httpd:2.4
RUN apt-get -y update && apt-get -y install nkf nano && \
rm -f /usr/local/apache2/htdocs/index.html && \
sed -ri 's/#LoadModule cgid_module/LoadModule cgid_module/g; \ 
             s/DirectoryIndex index.html/DirectoryIndex index.cgi/g; \ 
             s/Options Indexes FollowSymLinks/Options Indexes FollowSymLinks ExecCGI/g;              s/#AddHandler cgi-script .cgi/AddHandler cgi-script .pl .cgi/g' /usr/local/apache2/conf/httpd.conf

COPY cgi-bin /usr/local/apache2/cgi-bin
