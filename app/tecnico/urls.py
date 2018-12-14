from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.tec_list, name="index"),
    url('registrar/', views.registro_tec, name='registrar'),
]