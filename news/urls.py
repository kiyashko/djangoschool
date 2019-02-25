from django.urls import path

from .views import *


urlpatterns = [
    path("", PostList.as_view()),
    path("category/<slug:slug>/", PostList.as_view(), name="category_post"),
    path("<slug:slug>/", PostDetail.as_view(), name="post_detail"),
]
