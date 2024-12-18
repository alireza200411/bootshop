from django.urls import path
from . import views


app_name = 'product'
urlpatterns = [
    path('detail', views.detail, name='detail')
]
