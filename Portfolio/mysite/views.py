from django.shortcuts import render
from django.views.generic import  View
from .forms import *
from django.http import HttpResponseRedirect

# Create your views here.
class Main(View):
    def get(self, request):
        form = Forms(request.POST or None)
        context={'form':form}
        return render(request, 'index.html',context)

    def post(self, request):
        form = Forms(request.POST or None)
 
        if form.is_valid():
 
            Costomer.objects.create(first_name=request.POST['first_name'],email=request.POST['email'],comments=request.POST['context'])

          
            return HttpResponseRedirect('/')
        context={'form':form}
        return render(request, 'index.html',context)

    