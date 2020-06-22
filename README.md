Site  works on Ubuntu 18.0.4 

How to install on Ubuntu

sudo apt update
sudo apt install python3-pip python3-dev nginx curl 
sudo apt-get install -y gettext


#create virtual env
sudo -H pip3 install --upgrade pip
sudo -H pip3 install venv


mkdir ~/grusiner
cd ~/grusiner

virtualenv venv
source venv/bin/activate
pip install django gunicorn

#compilate ru to end messages
django-admin compilemessages
deactivate 

sudo vi /etc/systemd/system/gunicorn.socket

<!-- /etc/systemd/system/gunicorn.socket -->
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target 


sudo vi /etc/systemd/system/gunicorn.service
<!-- /etc/systemd/system/gunicorn.service -->
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=sammy
Group=www-data
WorkingDirectory=/home/grusiner/project/grusiner
ExecStart=/home/grusiner/project/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          grusiner.wsgi:application

[Install]
WantedBy=multi-user.target


sudo vi /etc/nginx/sites-available/grusiner
https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04#configure-nginx-to-proxy-pass-to-gunicorn

sudo ufw allow "Nginx Full"



#Install and configure SSL 
#Add two fields to server directory in nginx config

	ssl_certificate /etc/nginx/ssl/grusiner.crt;
    ssl_certificate_key /etc/nginx/ssl/grusiner.key; 

#setup static
#add  to  settings.py
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
    '/home/grusiner/project/venv/lib/python3.7/site-packages/django/contrib/admin/static/',
    )

#python3 manage.py collectstatic