from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from .models import Data, Math
from .forms import UploadFileForm
from django_boto.s3 import upload

# Create your views here.

# def owner_only(function):
# 	def wrap(request, *args, **kwargs):
# 	if request.user.profile.usertype == 1:
# 		return function(request, *args, **kwargs)
# 	else:
# 		return HttpResponseRedirect('/')
# 	wrap.__name__=function.__name__
# 	return wrap

def handle_uploaded_file(f):
    with open('data.csv', 'wb+') as destination:
    	for chunk in f.chunks():
    		destination.write(chunk)

@login_required(login_url='/registration/login/')
def upload_csv(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			upload(request.FILES['file'])
			print ("uploaded: ", request.FILES['file'])
			# handle_uploaded_file(request.FILES['file'])
			return HttpResponseRedirect('/repository/')
	else:
		form = UploadFileForm()
	return render_to_response('upload.html', {'form':form})

@login_required(login_url='/registration/login/')
def add(request):
	return render(request)


@login_required(login_url='/registration/login')
def index(request):
	data_list = Data.objects.all()
	context = {'data_list':data_list}
	return render(request, 'repository/index.html', context)


@login_required(login_url='registration/login')
def datum(request, data_id):
	data = get_object_or_404(Data, pk=data_id)
	return render(request, 'repository/datum.html')
