from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.order_list, name="index"),
    url('crear/', views.orden_crear, name='crear'),
    url('list/', views.order_li, name='orden_lista')
]