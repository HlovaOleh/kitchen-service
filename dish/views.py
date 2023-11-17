from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from cook.models import Cook
from .forms import (
    DishForm,
    DishTypeSearchForm,
    DishSearchForm,
)
from .models import DishType, Dish


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "num_cooks": Cook.objects.count(),
        "num_dish_types": DishType.objects.count(),
        "num_dish": Dish.objects.count(),
    }
    return render(request, "dish/custom-index.html", context=context)


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = "dishtype_list"
    template_name = "dish/dishtype_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishTypeSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = DishType.objects.all()
        form = DishTypeSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("dish:dish_type-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("dish:dish_type-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("dish:dish_type-list")


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Dish.objects.select_related("dish_type")
        form = DishSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("dish:dish-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("dish:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("dish:dish-list")


class DishCooksUpdateView(LoginRequiredMixin, generic.View):
    @staticmethod
    def post(
            request: HttpRequest,
            pk: int
    ) -> HttpResponseRedirect | HttpResponseBadRequest:
        try:
            dish = Dish.objects.get(pk=pk)
        except Dish.DoesNotExist:
            return HttpResponseBadRequest("Dish not found")

        cooks = dish.cooks

        if request.user in cooks.all():
            cooks.remove(request.user)
        else:
            cooks.add(request.user)

        return HttpResponseRedirect(reverse("dish:dish-detail", args=[pk]))
