from django.urls import path
from . import views

urlpatterns = [
    path('api/comment', views.comment_list),
];