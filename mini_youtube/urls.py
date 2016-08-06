from django.conf.urls import url
from django.contrib import admin
from youtube import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^youtube/$',views.PrincipalView.as_view(),name="matriz"),
    url(r'^youtube/(?P<slug>[-\w]+)/',views.DetailView.as_view(), name="detalle")
]
