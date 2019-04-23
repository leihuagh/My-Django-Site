from django.urls import path
from .views import index, experiences, portofolio, contact

app_name = 'aboutme'
urlpatterns = [
    path('', index, name='index'),
    path('experiences', experiences, name='experiences'),
    path('portofolio', portofolio, name='portofolio'),
    path('contact', contact, name='contact'),
]
