from django.urls import path
from .views import article_list, article_detail

urlpatterns = [
    path('articles/', article_list),
    path('article-detail/<int:pk>/', article_detail),
]