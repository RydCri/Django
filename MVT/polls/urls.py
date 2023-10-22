from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('polls/', views.polls, name='polls'),  # views/polls
    path("polls/<int:question_id>/", views.detail, name="detail"),
    path("polls/<int:question_id>/results/", views.results, name="results"),
    path("polls/<int:question_id>/vote/", views.vote, name="vote"),
]