from django.db import models
from django.core.urlresolvers import reverse

class Video(models.Model):
	titulo = models.CharField(max_length=200)
	photo = models.ImageField(upload_to='youtube/images/')
	url = models.CharField(max_length = 200)
	autor = models.CharField(max_length=100)
	slug = models.SlugField(max_length=500)
	ubimg = models.CharField(max_length=200,blank=True,null=True)

	def __str__(self):
			return self.titulo

	def get_absolute_url(self):
		return reverse('detalle',args=[self.slug])
