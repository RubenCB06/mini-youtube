from django.shortcuts import render
from django.views.generic import View
from .models import Video

class PrincipalView(View):
	def get(self,request):
		template_name = 'principal.html'
		videos = Video.objects.all().order_by('titulo')
		context = {'videos':videos,}
		#template_name = 'reproductor.html'
		return render(request,template_name,context)

class DetailView(View):
	def get(self,request,slug):
		template_name="reproductor.html"
		video = Video.objects.get(slug = slug)
		context = {
			'video':video,
		}
		return render(request,template_name,context)