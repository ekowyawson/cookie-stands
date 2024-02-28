from django.urls import path
from .views_front import (
    CookieStandCreateView,
    CookieStandDeleteView,
    CookieStandDetailView,
    CookieStandListView,
    CookieStandUpdateView,
)

urlpatterns = [
    path("", CookieStandListView.as_view(), name="cookie_stands_list"),
    path("<int:pk>/", CookieStandDetailView.as_view(), name="cookie_stands_detail"),
    path("create/", CookieStandCreateView.as_view(), name="cookie_stands_create"),
    path("<int:pk>/update/", CookieStandUpdateView.as_view(), name="cookie_stands_update"),
    path("<int:pk>/delete/", CookieStandDeleteView.as_view(), name="cookie_stands_delete"),
]
