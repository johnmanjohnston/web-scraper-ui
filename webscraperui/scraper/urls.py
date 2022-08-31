from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("search/<str:q>", views.search_page, name="search")
    path("search", views.search_page, name="search")
    
]