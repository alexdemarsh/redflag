from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.views import generic

from .models import Data, Math

from .forms import UploadFileForm

from django_boto.s3 import upload

from django.views.generic.base import TemplateView

# Create your views here.

# def owner_only(function):
# 	def wrap(request, *args, **kwargs):
# 	if request.user.profile.usertype == 1:
# 		return function(request, *args, **kwargs)
# 	else:
# 		return HttpResponseRedirect('/')
# 	wrap.__name__=function.__name__
# 	return wrap

@login_required(login_url='/registration/login/')
def upload_file(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			print request.FILES['file']
			data_url = upload(request.FILES['file'])
			#create new django model
			d = Data.objects.create(owner=request.user)
			d.name = request.POST['name']
			d.url = data_url
			d.description =request.POST['description']
			d.save()
		return HttpResponseRedirect('/repository/')
	else:
		form = UploadFileForm()
	return render(request,'upload.html', {'form': form})


@login_required(login_url='/registration/login/')
def upload_csv(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		data_url = upload(request.FILES['file'])
		if form.is_valid():
			data_url = upload(request.FILES['file'])
			print data_url
			print ("uploaded: ", request.FILES['file'])
			# handle_uploaded_file(request.FILES['file'])
			return HttpResponseRedirect('/repository/')
		else:
			print ("invalid form", form.errors)
	else:
		form = UploadFileForm()
	return render(request, 'upload.html', {'form':form})


# class IndexView(generic.ListView):
# 	template_name = 'repository/index.html'
# 	context_object_name = 'data_list'

# 	def get_queryset(self):
# 		return Data.objects.all()

@login_required(login_url='/registration/login')
def index(request):
	data_list = Data.objects.all()
	context = {'data_list':data_list}
	return render(request, 'repository/index.html', context)


@login_required(login_url='registration/login')
def datum(request, data_id):
	datum = Data.objects.get(pk=data_id)
	context = {'datum':datum}
	return render(request, 'repository/datum.html', context)


class HomePageView(TemplateView):

    template_name = "repository/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['data_list'] = Data.objects.all()
        return context