from django.urls import path

# from .models import Article
# from config.urls import urlpatterns
from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleCreateView,
    AdminPageView,
)

urlpatterns = [
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_create'),
    path('', ArticleListView.as_view(), name = 'article_list'),
    path('superuser/',AdminPageView.as_view(), name='superuser_page'),
]