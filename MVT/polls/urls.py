from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('polls/', views.polls, name='polls'),  # views/polls
    path("polls/createPoll", views.new_poll, name="new_poll"),
    path("polls/createChoice", views.new_choice, name="new_choice"),
    path("polls/<int:question_id>/", views.detail, name="detail"),
    path("polls/<int:question_id>/results/", views.results, name="results"),
    path("polls/<int:question_id>/vote/", views.vote, name="vote"),
]
