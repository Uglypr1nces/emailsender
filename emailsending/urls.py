from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('send_email', views.send_email, name='send_email')
]
