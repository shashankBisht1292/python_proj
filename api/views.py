from rest_framework import viewsets, status
from .serializers import ArticleSerializer
from .models import Article
from rest_framework import mixins

class GenericViewSetView(viewsets.GenericViewSet, mixins.ListModelMixin,
                         mixins.CreateModelMixin, mixins.UpdateModelMixin,
                         mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
