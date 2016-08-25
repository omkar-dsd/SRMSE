from django.views import generic
from .models import Album

class IndexView(generic.ListView):
	template_name = 'music/index.html'
	context_object_name = 'all_albums'
	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/detail.html'
	
		
	
		
























# # from django.http import Http404
# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from django.template import loader  #for html templates
# from .models import Album, Song 


# def index(request):

# 	all_albums = Album.objects.all()     #creates a list 
	
# 	# template = loader.get_template('music/index.html') #django already looks into templates directory

# 	# context = {	'all_albums': all_albums }
# 	return render(request, 'music/index.html', {'all_albums': all_albums})


# def detail(request, album_id):
# 	# try:
# 	# 	album = Album.objects.get(pk=album_id)
# 	# except Album.DoesNotExist:
# 	# 	raise Http404("Album does not exist")
# 	album = get_object_or_404(Album, pk=album_id)    #shortcut to above code
# 	return render(request, 'music/detail.html', {'album': album })

# def favourite(request, album_id):
# 	album = get_object_or_404(Album, pk=album_id)    #shortcut to above code
# 	try:
# 		selected_song = album.song_set.get(pk=request.POST['song'])
# 	except (KeyError, Song.DoesNotExist):
# 		return render(request, 'music/detail.html', {
# 			'album': album,
# 			'error_message': "You did not select a valid song"
# 			})	

# 	else:
# 		selected_song.is_favourite = True
# 		selected_song.save()
# 		return render(request, 'music/detail.html', {'album': album})





# # Create your views here.
