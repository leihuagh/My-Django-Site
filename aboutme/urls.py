from django.urls import path
from .views import index

app_name = 'aboutme'
urlpatterns = [
    path('', index, name='index'),
]
