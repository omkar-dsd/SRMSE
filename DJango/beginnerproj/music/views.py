# from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader  #for html templates
from .models import Album 


def index(request):

	all_albums = Album.objects.all()     #creates a list 
	
	# template = loader.get_template('music/index.html') #django already looks into templates directory

	# context = {	'all_albums': all_albums }
	return render(request, 'music/index.html', {'all_albums': all_albums})


def detail(request, album_id):
	# try:
	# 	album = Album.objects.get(pk=album_id)
	# except Album.DoesNotExist:
	# 	raise Http404("Album does not exist")
	album = get_object_or_404(Album, pk=album_id)    #shortcut to above code
	return render(request, 'music/detail.html', {'album': album })




# Create your views here.
