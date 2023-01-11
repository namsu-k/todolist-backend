from django.urls import path
from . import views

urlpatterns = [
    path("", views.Todolist.as_view()),
    path("<int:pk>", views.Todoitem.as_view()),
]
