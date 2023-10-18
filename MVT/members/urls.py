from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #views/index
    path('members/', views.members, name='allmembers'), #views/members
    path('members/details/<int:id>', views.details, name='details'),]
