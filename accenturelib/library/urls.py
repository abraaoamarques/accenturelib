from django.urls import path
from . import views
from .views import BookList, BookSingle

urlpatterns = [
    path('api/comment', views.comment_list),
    path('api/book/', BookList.as_view()),
    path('api/book/<str:id>', BookSingle.as_view()),
];