from django.urls import path, re_path
from . import views

urlpatterns = [
    path("blog_index/", views.blog_index, name="blog_index"),
    # path("blog/", views.blog_list, name="blog_list"),
    path("about/", views.about, name="about"),
    path("post/<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path("tag/<tag>/", views.blog_tag, name="blog_tag"),
]
