from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *
# Create your views here.
#Returing string html using Function Based View
def fbv_string(request):
    return HttpResponse('<h1>fbv_string is done</h1>')

#Returing string html using Class Based View
class cbv_string(View):
    def get(self,request):
        return HttpResponse('<h1>cbv_string is done</h1>')

#Rendering the html page using Function Based View
def fbv_rendering(request):
    return render(request,'fbv_rendering.html')

#Rendering the html page using Class Based View
class cbv_rendering(View):
    def get(self,request):
        return render(request,'cbv_rendering.html')

#Insert data using Function Based View
def insert_school_by_fbv(request):
    ESFO = SchoolForm()
    d = {'ESFO':ESFO}

    if request.method == 'POST':
        SFDO = SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insert_school_by_fbv is done')
    return render(request,'insert_school_by_fbv.html',d)

#Insert data using Class Based View
class insert_school_by_cbv(View):
    def get(self,request):
        ESFO = SchoolForm()
        d = {'ESFO':ESFO}
        return render(request,'insert_school_by_cbv.html',d)

    def post(self,request):
        SFDO = SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insert_school_by_cbv is done')

#Code Reuseability using TemplateView
class cbv_TemplateView(TemplateView):
    template_name = 'cbv_TemplateView.html'