from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('predict/', views.predict_image, name='predict_image'),
]