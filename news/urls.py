from django.urls import path, include
from. import views

urlpatterns = [
    path('headline', views.index, name='this is news headline page'),
]