from django.contrib import admin
from .models import Video

class VideoAdmin(admin.ModelAdmin):
	list_display = ('titulo','photo','url','ubimg')
	search_fields = ('titulo',)
	prepopulated_fields = {'slug':('titulo',)}

admin.site.register(Video, VideoAdmin)
