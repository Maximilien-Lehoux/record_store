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
# Déclarer l'app dans settings-installed_app : 'store.apps.StoreConfig,'

# Ajouter un dossier templates dans l'app store
# Ajouter un dossier du nom de l'app (store) dans le dossier templates

# séparer les url de l'application avec les url du projet
# urls.py qui gère les route de l'application
# et url.py pour toutes les applications
# crééer urls.py dans store
# Modifier les urls du projet :
# rajouter url(r'^store/', include('store.urls')), dans url patterns (expression régulière)

# Ajouter dans les url de l'app store :
# from django.conf.urls import url  # importer les urls du projet
# from . import views  # import views so we can use them in urls.
# urls qui commencent ou termine par une chaine vide est relié à la vue index
# urlpatterns = [
#url(r'^$', views.index),  # "/store" will call the method "index" in "views.py"

# page accueil, appeler la vue index :
# modifier url du projet pour appeler la vue index