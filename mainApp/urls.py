from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    url('^AllPhoto/$', views.all_photo.as_view()),
    url('^$', views.main_page),
    url('^MyPhoto/$', views.my_picture),
    path('<int:pk>/', views.image_views.as_view()),
]