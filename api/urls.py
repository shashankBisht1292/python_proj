from django.urls import path
#from .views import article_list, article_detail
#from .views import ArticleAPIView, ArticleAPIDetail
from .views import ViewSetView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('articles', ViewSetView, basename='arti')
urlpatterns = router.urls


# urlpatterns = [
#     path('articles/', article_list),
#     path('articles/', ArticleAPIView.as_view()),
#     path('article-detail/<int:pk>/', article_detail),
#     path('article-detail/<int:pk>/', ArticleAPIDetail.as_view()),
#     path('articles/', ViewSetView.as_view({'get': 'list'})),
#     path('articles/<int:pk>/', ViewSetView.as_view({'get': 'retrieve'})),
# ]