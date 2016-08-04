from django.shortcuts import render
from django.views.generic import View

class PrincipalView(View):
	def get(self,request):
		template_name = 'principal.html'
		#template_name = 'reproductor.html'
		return render(request,template_name)