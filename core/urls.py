from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from home.views import index

urlpatterns = [
    path('', index, name='index'),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout')
]
