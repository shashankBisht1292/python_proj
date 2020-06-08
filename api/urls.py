from django.urls import path
#from .views import article_list, article_detail
#from .views import ArticleAPIView, ArticleAPIDetail
from .views import GenericAPIView

urlpatterns = [
    #path('articles/', article_list),
    #path('articles/', ArticleAPIView.as_view()),
    #path('article-detail/<int:pk>/', article_detail),
    #path('article-detail/<int:pk>/', ArticleAPIDetail.as_view()),
    path('articles/', GenericAPIView.as_view()),
    path('articles/<int:pk>/', GenericAPIView.as_view()),
]