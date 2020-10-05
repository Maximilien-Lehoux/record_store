from django.conf.urls import url  # importer les urls du projet

from . import views  # import views so we can use them in urls.

# urls qui commencent ou termine par une chaine vide est relié à la vue index
urlpatterns = [
    url(r'^$', views.listing),  # "/store" will call the method "index" in "views.py"
    url(r'^(?P<album_id>[0-9]+)/$', views.detail),
]