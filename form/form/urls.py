from django.contrib import admin
from django.urls import path
from FormApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('appointment', views.index),
    path('form', views.form),
    path('order', views.order)
]


