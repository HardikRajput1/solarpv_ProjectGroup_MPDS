from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('portalform', views.portalform, name='portalform'),
    path('client_form', views.client_form, name='client_form'),
    path('location_form', views.location_form, name='location_form'),
    path('product_form', views.product_form, name='product_form'),
    path('test_standard_form', views.test_standard_form, name='test_standard_form'),
    path('certificate_form', views.certificate_form, name='certificate_form'),
]