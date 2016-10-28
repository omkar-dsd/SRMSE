from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class DiaryWriter(models.Model):

	first_name = models.CharField(max_length = 250)
	last_name =  models.CharField(max_length = 250)

		#This function redirects after clicking the submit button
	def get_absolute_url(self):
		return reverse('indiariez:detail', kwargs = {'pk': self.pk})


	def __str__(self):
		return self.first_name + self.last_name



class Diary(models.Model):

	writer = models.ForeignKey(DiaryWriter, on_delete = models.CASCADE)
	topic = models.CharField(max_length = 250)
	subtitle = models.CharField(max_length = 500)
	category = models.CharField(max_length = 250)
	diary_file = models.FileField()


	def get_absolute_url(self):
		return reverse('indiariez:song-index')

	def __str__(self):
		return self.topic 

