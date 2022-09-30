from tempfile import template
from django.views import generic

from pims.forms import containerForm

# Create your views here.

from .models import item, container, item_container, season

from django.db import connection

# http://localhost:8000/
class IndexView(generic.TemplateView):
    template_name = 'pims/index.html'
    model = container

# http://localhost:8000/allItems/
class itemListView(generic.ListView):
    template_name = 'pims/item_list.html'
    model = item
    context_object_name = 'item'
    def get_queryset(self):
        return item.objects.all().order_by('name')

# http://localhost:8000/allcontainers/
class containerListView(generic.ListView):
    template_name = "pims/container_list"
    model = container
    context_object_name = 'container'
    def get_queryset(self):
        return container.objects.all().order_by('location')

# http://localhost:8000/contents/11
class contentsView(generic.ListView):
    template_name = "pims/contents.html"
    model = container
    context_object_name = 'container'
    def get_queryset(self):
        newContainer = container.objects.get(id=self.kwargs['pk'])
        print(connection.queries)
        return newContainer.item_container_set.all()


# * Above views are working as desired


class itemDetailView(generic.DetailView):
    model = item
    template_name: 'pims/itemDetails.html'



class editIC(generic.UpdateView):
    template_name = "pims/editItems.html"
    model = item_container
    context_object_name = 'item'
    fields = {
        'item',
        'quantity',
        'container'
    }
    success_url="../allItems/"

class editItem(generic.UpdateView):
    template_name = "pims/editItems.html"
    model = item
    context_object_name = 'item'
    fields = {
        'name'
    }
    success_url="../../allItems/"

class editContainer(generic.UpdateView):
    template_name = "pims/editItems.html"
    model = container
    context_object_name = 'item'
    form_class = containerForm
    success_url="../../allContainers/"

class addICView(generic.CreateView):
    model = item_container
    template_name = 'pims/additemscontainer.html'
    fields = {
        'item',
        'quantity',
        'container'
    }
    success_url="../allItems/"

class additemView(generic.CreateView):
    model = item
    template_name = 'pims/add.html'
    fields = {
        'name'
    }
    success_url="../allItems/"

class addcontainerView(generic.CreateView):
    model = container
    template_name = 'pims/add.html'
    success_url="../allcontainers/"
    form_class = containerForm

class deleteitem(generic.DeleteView):
    model = item
    template_name = 'pims/deleteitems.html'
    success_url = "../allItems/"

class deleteContainer(generic.DeleteView):
    model = container
    template_name = 'pims/deleteitems.html'
    success_url = "../allContainers/"


class styleGuide(generic.ListView):
    template_name = 'pims/styleGuide.html'
    def get_queryset(self):
        return ''

class sitePlan(generic.ListView):
    template_name = 'pims/sitePlan.html'
    def get_queryset(self):
        return ''


class test(generic.ListView):
    model = item_container
    template_name = 'pims/test.html'



#TODO
class seasonView(generic.ListView):
    model = season
    template_name = 'pims/season.html'
    context_object_name = 'season'
    def get_queryset(self):
        newSeason = season.objects.get(id=self.kwargs['pk'])
        return newSeason.container.all()
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['item'] = item.objects.all()
    #     return False