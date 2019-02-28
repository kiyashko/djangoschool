from django.urls import path

from .views import *


urlpatterns = [
    path("", PostList.as_view(), name="news"),
    path("category/<slug:slug>/", PostList.as_view(), name="category_post"),
    path("<slug:slug>/", PostDetail.as_view(), name="post_detail"),
    path("comment/<slug:slug>/", PostDetail.as_view(), name="add_comment"),
]
