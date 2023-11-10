from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from restaurant.models import Cook, DishType, Dish


def index(request: HttpRequest) -> HttpResponse:
    num_cooks = Cook.objects.count()
    num_dish_types = DishType.objects.count()
    num_dish = Dish.objects.count()
    context = {
        "num_cooks": num_cooks,
        "num_dish_types": num_dish_types,
        "num_dish": num_dish
    }
    return render(request, "restaurant/index.html", context=context)
