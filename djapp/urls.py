from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage),
	path('api',views.gettext),
	path('guide',views.guide)
]