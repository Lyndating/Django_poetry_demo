from django.urls import path

from . import views
# from current repo import views.py

urlpatterns = [
    # index view: /polls/
    path('', views.index, name='index'),
    # single view: /polls/:id/
    path('<int:question_id>/', views.detail, name='detail'),
    # single result view: /polls/:id/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # single vote view: /polls/:id/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]