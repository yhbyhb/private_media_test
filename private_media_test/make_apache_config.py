import os

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

configuration = '''
<VirtualHost *:80>
        # The ServerName directive sets the request scheme, hostname and port t$
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header to
        # match this virtual host. For the default virtual host (this file) this
        # value is not decisive as it is used as a last resort host regardless.
        # However, you must set it for any further virtual host explicitly.
        ServerName cse.yonsei.ac.kr

        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html

        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
        # error, crit, alert, emerg.
        # It is also possible to configure the loglevel for particular
        # modules, e.g.
        #LogLevel info ssl:warn

        ErrorLog ${{APACHE_LOG_DIR}}/error.log
        CustomLog ${{APACHE_LOG_DIR}}/access.log combined

        # For most configuration files from conf-available/, which are
        # enabled or disabled at a global level, it is possible to
        # include a line for only one particular virtual host. For example the
        # following line enables the CGI configuration for this host only
        # after it has been globally disabled with "a2disconf".
        #Include conf-available/serve-cgi-bin.conf

        Alias /static {0}/static
        <Directory {0}/static>
            Require all granted
        </Directory>

        Alias /media {0}/media
        <Directory {0}/media>
            Require all granted
        </Directory>

        <Directory {0}/{1}>
            <Files wsgi.py>
                Require all granted
            </Files>
        </Directory>

        XSendFile on
        XSendFilePath {0}/private
        Alias /private {0}/private
        <Directory {0}/private>
            Order Deny,Allow
            Allow from all
        </Directory>

        WSGIDaemonProcess {1} python-path={0}/
        WSGIProcessGroup {1}
        WSGIScriptAlias / {0}/{1}/wsgi.py

        WSGIPassAuthorization On
</VirtualHost>
'''

print configuration.format(CUR_DIR, "private_media_test")