python manage.py makemigrations
python manage.py migrate
sudo python manage.py collectstatic
sudo chown www-data ../private_media_test -R
sudo service apache2 restart