from django.urls import path
from serializer_1.api.views import article_list_create_api_view, article_detail_create_api_view

urlpatterns =[
path("articles/", article_list_create_api_view, name="article-list"),
path("articles/<int:pk>/", article_detail_create_api_view, name="article-detail"),
]
