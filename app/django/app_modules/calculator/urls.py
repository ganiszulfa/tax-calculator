from django.conf.urls import url 

from . import views

urlpatterns = [
    url(r'^$', views.index, name='add_tax_object'),
    url(r'^view-my-bill/$', views.view_my_bill, name='view_my_bill'),
    url(r'api/tax_object/$', views.tax_object_list),
    url(r'api/tax_object/(?P<pk>[\w-]+)/$', views.tax_object_detail),
]

