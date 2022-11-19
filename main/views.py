from multiprocessing import context
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth import login



class HomeView(TemplateView):
    template_name = 'main/index.html'
