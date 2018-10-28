# django-apollo-forms
Dinamic forms using django framework

Project to create dinamic forms application using Django web framework

## Built With

* [Python](https://www.python.org) - Programming language
* [Django](https://www.djangoproject.com) - The web framework used
* [Django-fobi](https://github.com/barseghyanartur/django-fobi) - Form generator/builder application for Django

## Versions
BETA

# Installation
## Prerequisites

- Python >= 3.6.x

- pip or pip3
- virtualenv
- virtualenvwrapper
```
$ python -V o python3 -V
$ Python 3.6.6
$ pip -V
$ "command not found"
$ pip3 install --upgrade pip
$ pip -V
$ pip 18.0 from /Library/Frameworks/..../pip (python 3.6)
$ pip install --upgrade pip
$ pip install virtualenv virtualenvwrapper
```
## Getting Started

```git clone https://[username]@bitbucket.org/enriquemt/fobi.git```

#### Creating the develop  environment

```
[user_home]$ mkdir .virtualenv
$ nano .virtualenv
# add this
export WORKON_HOME=$HOME/.virtualenvs
# change the path to virtualenvwrapper.sh because depends of your system
source /Library/Frameworks/Python.framework/Versions/3.6/bin/virtualenvwrapper.sh (change the path if necessary)
export PIP_VIRTUALENV_BASE=$WORK_HOME 
```
##### Create a virtual environment
```
$ virtualenv apollo
$ source .virtualenv/apollo/bin/activate
(apollo)$ command...
```
### Installing

Go to folder that you had cloned the git project. 

```
(apollo)$ cd [django_site_root_folder]
(apollo)$ pip install -r requirements.txt
(apollo)$ python manage.py migrate
(apollo)$ python manage.py createsuperuser --username admin
(apollo)$ python manage.py runserver [IP:][port number optional ex. 8000 or 127.0.0.1:8000]
```

**Open your browser and navigate to [here](http://localhost:8000)**

* http://localhost:8000
* super user [administration](http://localhost:8000/admin): admin / apolloadm1n
* usuarios agentes:
    * agente1 / apolloadm1n
    * agente2 / apolloadm1n

## django-admin and manage.py commands
- [django-admin and manage.py commands (ES)](https://docs.djangoproject.com/es/2.1/ref/django-admin)
- [django-admin and manage.py commands (EN)](https://docs.djangoproject.com/en/2.1/ref/django-admin)

## Reset and rebuild

This will IRREVERSIBLY DESTROY all data currently in the database,
and return each table to an empty state.

```
(apollo)$ cd [django_site_root_folder]
(apollo)$ python manage.py showmigrations
(apollo)$ python manage.py flush
(apollo)$ python manage.py migrate
(apollo)$ python manage.py createsuperuser --name=admin --email=adminnoreal@apollo.apo
(apollo)$ python manage.py runserver
```

## Create a new django application

```
(apollo)$ cd [django_site_root_folder]
(apollo)$ python manage.py startapp [application name]
```
###### Result

```
app_name/
    migrations/
        __init__.py
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
```
- views.py is the file to create the views for call the view we need to assign the view to a URL to do that we need create a URLConf in urls.py file.
- urls.py is the file to create de URLConf.
- At last we need to add this urls.py file with the URLConf in the root of the django site in the main file urls.py, the main file urls.py is into the folder that contains settings.py.
- If you need more information about django framework works review the django documentation: 
    - [Django website](https://www.djangoproject.com)
    - [Django website Documentation 2.1 (ES)](https://docs.djangoproject.com/es/2.1/)
    - [Django website Documentation 2.1 (EN)](https://docs.djangoproject.com/en/2.1/)

## License

License
=======
GPL 3.0
