from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import ListView,TemplateView,DetailView,CreateView,UpdateView,DeleteView

from app.models import *

class Home(TemplateView):
    template_name='app/home.html'

class SchoolList(ListView):
    model=School
    context_object_name='schools'
    template_name='app/SchoolList.html'
    #queryset=School.objects.filter(name='jsp')
    ordering=['location']

class SchoolDetail(DetailView):
    model=School
    context_object_name='i'

class SchoolCreate(CreateView):
    model=School
    fields='__all__'

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'

class SchoolDelete(DeleteView):
    model=School
    context_object_name='i'
    success_url=reverse_lazy('SchoolList')