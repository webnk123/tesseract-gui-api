from django.shortcuts import render
from .img2text import convertimg
import os
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import shutil


def homepage(request):
	if request.method == "POST":
		lang = request.POST.get('lang')
		f = request.FILES['sentFile']
		file_name = 'filename' + os.path.splitext(f.name)[-1]
		response = convertimg(file_name,lang, f)
		return render(request,'djapp/home.html', response)
	else:
		return render(request, 'djapp/home.html')




@api_view(['POST'])
@csrf_exempt
def gettext(request):
	lang = request.data.get('lang')
	f = request.data.get('image')
	file_name = 'filename' + os.path.splitext(f.name)[-1]
	data=convertimg(file_name,lang,f)
	return Response(data=data)

def guide(request):
	return render(request, 'djapp/api_guide.html')