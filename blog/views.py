from django.contrib import messages
from django.shortcuts import get_list_or_404, render
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin

from .models import Article, Category


# Create your views here.
class CategoryListView(ListView):
    model = Category
    template_name = "blog/list.html"


class ArticleListView(ListView):
    model = Article
    template_name = "blog/list.html"


class ArticleCategoryView(ListView):
    def get_queryset(self, *args, **kwargs):
        article_list = get_list_or_404(Article, category_id=kwargs.get("id"))
        return article_list

    template_name = ""


class ArticleDetailView(FormMixin, DetailView):
    model = Article
    template_name = ""
    slug_field = "id"
    slug_url_kwarg = "id"
    form_class = ""

    def get_success_url(self):
        return reverse("", kwargs={"id": self.object.id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        apply = form.save()
        apply.job = self.get_object()
        apply.save()
        messages.success(self.request, "", "")
        return super(ArticleDetailView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "", "")
        return super(ArticleDetailView, self).form_invalid(form)
