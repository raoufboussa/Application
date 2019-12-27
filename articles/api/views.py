from .serializers import *
from ..models import Article
from rest_framework.generics import ListAPIView, RetrieveAPIView  

class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers

class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers