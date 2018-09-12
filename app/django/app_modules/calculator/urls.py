from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='add_tax_object'),
    url(r'^view-my-bill/$', views.view_my_bill, name='view_my_bill'),
]
