from django.urls import path

from .views import (
    index,
    DishTypeListView,
    DishListView,
    DishDetailView,
    CookListView,
    CookDetailView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "dish_types/",
        DishTypeListView.as_view(),
        name="dish_type-list"
    ),
    path(
        "dish_types/create/",
        DishTypeCreateView.as_view(),
        name="dish_type-create",
    ),
    path(
        "dish_types/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish_type-update",
    ),
    path(
        "dish_types/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish_type-delete",
    ),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path(
        "cooks/<int:pk>/",
        CookDetailView.as_view(),
        name="cook-detail"
    ),
]

app_name = "restaurant"
