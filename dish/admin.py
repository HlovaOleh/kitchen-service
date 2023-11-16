from django.contrib import admin
from .models import DishType, Dish


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "price", "dish_type"]
    list_filter = ["dish_type__name", ]
    search_fields = ["name", ]
