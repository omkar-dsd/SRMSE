from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View 
from .models import Album, Song
from .forms import UserForm



class IndexView(generic.ListView):
	template_name = 'music/index.html'
	context_object_name = 'all_albums'
	def get_queryset(self):
		return Album.objects.all()