from typing import Any
from django.shortcuts import render,redirect
from .models import Memoire
from .forms import MemoireForm
from django.urls import reverse,reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView


class MemoireCreateView(CreateView):
    model = Memoire
    form_class = MemoireForm
    template_name = 'admin/memoire/create.html'
    success_url = reverse_lazy('memoire:index')
    
class MemoireListView(ListView):
    model = Memoire
    context_object_name = 'memoires'
    template_name = 'admin/memoire/index.html'
    
class MemoireUpdateView(UpdateView):
    model = Memoire
    form_class = MemoireForm
    template_name = 'admin/memoire/update.html'
    context_object_name = 'memoires'
    success_url = reverse_lazy('memoire:index')
    
class MemoireDetailView(DetailView):
    model = Memoire
    context_object_name = 'memoires'
    template_name = 'admin/memoire/detail.html'
    
class MemoireDeleteView(DeleteView):
    model = Memoire
    template_name = 'admin/memoire/index.html'
    success_url = reverse_lazy('memoire:index')