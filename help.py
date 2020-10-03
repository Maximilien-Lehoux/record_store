# virtual env :
# virtualenv -p python3 env

# activer environnement virtuel :
# env\Scripts\activate.bat (cmd)

# Désactiver environnement virtuel :
# desactivate (cmd)

# version django :
# python -m django --version (cmd)

# Créér projet django
# django-admin startproject nom_projet_django (cmd)

# Base de donnée django (postgresql)
# pip install psycopg2

# Installer posgresql windows via le site

# Activation django :
# python manage.py runserver
# $ python manage.py makemigrations
# $ python manage.py migrate

# modifier dasns settings : la langue (fr) et TIME_ZONE = 'Europe/Paris'

# django debug toolbar qui permet de manipuler une barre qui donne plusieurs fonctionnalité pendant le developpement
# pip install django-debug-toolbar
# dans settings.py dans installed_apps, rajouter 'debug_toolbar',
# rajouter le middleware : 'debug_toolbar.middleware.DebugToolbarMiddleware',
# INTERNAL_IPS = ['127.0.0.1'] à la fin après static_url

# dans urls.py
# from django.contrib import admin
# from django.urls import path
# from django.conf import settings
# from django.conf.urls import include, url
# if settings.DEBUG:
    # import debug_toolbar
    # urlpatterns = [
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    # ] + urlpatterns

# Création d'une nouvelle application django :
# django-admin startapp store (cmd)
