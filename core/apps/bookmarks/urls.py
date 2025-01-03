"""Bookmark urls."""

from django.urls import path

from .views import (
    BookmarkCategoryListView,
    BookmarkCategoryRetrieveUpdateDestroyView,
    BookmarkCreateView,
    BookmarkDestoryView,
)

urlpatterns = [
    path(
        "categories/", BookmarkCategoryListView.as_view(), name="bookmark_category_list"
    ),
    path(
        "<uuid:article_id>/",
        BookmarkCreateView.as_view(),
        name="bookmark_create",
    ),
    path(
        "category/<slug:slug>/<uuid:article_id>/",
        BookmarkDestoryView.as_view(),
        name="bookmark_delete",
    ),
    path(
        "category/<slug:slug>/",
        BookmarkCategoryRetrieveUpdateDestroyView.as_view(),
        name="bookmark_category_retrieve_update_destroy",
    ),
]
