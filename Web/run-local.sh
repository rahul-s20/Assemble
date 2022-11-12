
export DB='gather_dev'
export DB_HOST='localhost'
export DB_PORT='5432'
export DB_USER='postgres'
export DB_PASSWORD='123456789'

echo "********************** Sarc-Gather **************************"
#python manage.py startapp home

python manage.py runserver