from django.urls import path

from .views import mainpage

app_name = 'tree_app'

urlpatterns = [
    path('main/', mainpage, name='main'),
]
