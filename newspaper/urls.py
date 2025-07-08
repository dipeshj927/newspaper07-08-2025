"""
URL configuration for NEWS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from newspaper import views

urlpatterns = [
    path(
        "",
        views.HomeView.as_view(),
        name="home",
    ),
    path(
        "about/",
        views.AboutView.as_view(),
        name="about",
    ),
    path(
        "contact/",
        views.ContactView.as_view(),
        name="contact",
    ),
    path(
        "post-list/",
        views.PostListView.as_view(),
        name="post-list",
    ),
    path(
        "post-detail/<int:pk>/",
        views.PostDetailView.as_view(),
        name="post-detail",
    ),
    path(
        "post-by-category/<int:category_id>/",
        views.PostByCategoryView.as_view(),
        name="post-by-category",
    ),
    path(
        "post-by-tag/<int:tag_id>/",
        views.PostByTagView.as_view(),
        name="post-by-tag",
    ),
    path(
        "newsletter/",
        views.NewsletterView.as_view(),
        name="newsletter",
    ),
    path(
        "comment/",
        views.CommentView.as_view(),
        name="comment",
    ),
    path(
        "search/",
        views.PostSearchView.as_view(),
        name="search",
    ),
]
