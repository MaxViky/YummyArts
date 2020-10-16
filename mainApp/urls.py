from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$', views.mainPage.as_view()),
    url('^MyPhoto/$', views.my_picture),
]