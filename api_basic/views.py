from .models import Article
from .serializers import ArticleSerializer
from rest_framework import generics, mixins

# Create your views here.


class ArticleAPIView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, id=None, *args, **kwargs):
        return self.update(request, id, *args, **kwargs)

    def delete(self, request, id=None, *args, **kwargs):
        return self.destroy(request, id, *args, **kwargs)