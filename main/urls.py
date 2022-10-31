from django.urls import path
from . import views


urlpatterns = [
path('',views.home, name='home'),
path("gallery/", views.gallery, name="gallery"),
path("faqs/", views.faqs, name="faqs"),
# path("faqs/", views.faqs, name="faqs"),
# path("milestone/", views.milestone, name="milestone"),
# path("resources/", views.resources, name="resources"),
# path('category/<slug:slug>', views.categoryPage, name='image-category'),
# path('category/<slug:slug1>/<slug:slug2>', views.imageDetailPage, name='image-detail'),
]
