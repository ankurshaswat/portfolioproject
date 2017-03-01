from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_message, name='index'),
    url(r'^message/',views.get_message,name='message'),
    url(r'^thanks/',views.thanks,name='thanks'),
]
