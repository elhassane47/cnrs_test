from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from core.models import Brand, Tablet
from core.forms import TabletForm, BrandForm
from django.shortcuts import reverse


class TabletList(ListView):
    model = Tablet
    ordering = ['-name']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['french'] = Tablet.objects.filter(brand__country="FR", release_year__year__gt=2015, release_year__year__lt=2020)
        context['object_list'] = Tablet.objects.exclude(pk__in=context['french'].values('pk'))
        return context


class TabletDetail(DetailView):
    model = Tablet


class TabletCreate(CreateView):
    model = Tablet
    form_class = TabletForm

    def get_success_url(self):
        return reverse('tablets-list')


class TabletUpdate(UpdateView):

    model = Tablet
    form_class = TabletForm

    def get_success_url(self):
        return reverse('tablets-list')


class TabletDelete(DeleteView):

    model = Tablet

    def get_success_url(self):
        return reverse('tablets-list')


class BrandCreate(CreateView):
    model = Brand
    form_class = BrandForm

    def get_success_url(self):
        return reverse('tablets-list')



