from django.urls import path

from .views import (
    CookListView,
    CookDetailView,
    CookCreateView,
    CookDeleteView,
    CookUpdateView,
    CookChangePasswordView
)

urlpatterns = [
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path(
        "cooks/<int:pk>/",
        CookDetailView.as_view(),
        name="cook-detail"
    ),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/delete/",
         CookDeleteView.as_view(),
         name="cook-delete"),
    path("cooks/<int:pk>/info_update/",
         CookUpdateView.as_view(),
         name="cook-update"),
    path("cooks/<int:pk>/password_update/",
         CookChangePasswordView.as_view(),
         name="cook-password-update"),
]

app_name = "cook"
