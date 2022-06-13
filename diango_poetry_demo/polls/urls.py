from django.urls import path

from . import views
# from current repo import views.py

app_name = 'polls'
urlpatterns = [
    # index view: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # single view: /polls/:id/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # single result view: /polls/:id/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # single vote view: /polls/:id/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]