
from rest_framework.routers import DefaultRouter

from article.viewsets import ArticleViewset

router = DefaultRouter()
router.register(r'article', ArticleViewset)