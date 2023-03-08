from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('',views.welcome, name='welcome'),
    path('join/',views.join, name='join'),
    path('inmusician/',views.inmusician, name='musicianin'),
]
