from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from restaurant.models import Cook, DishType, Dish


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "num_cooks": Cook.objects.count(),
        "num_dish_types": DishType.objects.count(),
        "num_dish": Dish.objects.count()
    }
    return render(request, "restaurant/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType
    queryset = DishType.objects.all()
    paginate_by = 5


class DishListView(generic.ListView):
    model = Dish
    queryset = Dish.objects.select_related("dish_type")
    paginate_by = 5


class DishDetailView(generic.DetailView):
    model = Dish


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 5


class CookDetailView(generic.DetailView):
    model = Cook
    queryset = Cook.objects.all()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["dish_list"] = self.object.cooks.select_related("dishes")
        return context
