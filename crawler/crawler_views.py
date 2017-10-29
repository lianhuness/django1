# coding=utf-8
# author= YQZHU
from django.shortcuts import render

# Create your views here.

from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView

from .keyword_models import Keyword

class list_keywords(ListView):
    model = Keyword
    template_name = "keywords/list_keywords.html"

class keyword_add(CreateView):
    model = Keyword
    fields=('words',)
    success_url = reverse_lazy('keywords-list')

class keyword_delete(DeleteView):
    model = Keyword
    success_url = reverse_lazy('keywords-list')
