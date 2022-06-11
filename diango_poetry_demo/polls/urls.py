from django.urls import path

from . import views
# from current repo import view file

urlpatterns = [
    path('', views.index, name='index'),
]