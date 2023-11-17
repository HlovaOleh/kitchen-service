from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views import generic

from .forms import (
    CookCreateForm,
    CookUpdateForm,
    CookSearchForm
)
from .models import Cook


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = CookSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = Cook.objects.all()
        form = CookSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    queryset = Cook.objects.prefetch_related("dishes__dish_type")


class CookCreateView(generic.CreateView):
    model = Cook
    form_class = CookCreateForm


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("cook:cook-list")


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookUpdateForm
    success_url = reverse_lazy("cook:cook-list")


class CookChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    model = Cook
    template_name = "change_password.html"
    success_url = reverse_lazy("cook:cook-list")
