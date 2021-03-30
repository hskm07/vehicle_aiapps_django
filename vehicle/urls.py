from django.urls import path
from . import views

app_name = 'vehicle'
urlpatterns = [
    path('predict/', views.predict, name='predict'),
    path('', views.index, name='index'),
    
]