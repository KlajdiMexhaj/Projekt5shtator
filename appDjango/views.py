from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    kategori = Kategori.objects.all()
    items = Item.objects.all()
    context = {"Items_value":items,"Kategori_data":kategori}
    return render(request,'home.html',context)

def about(request):
    staffs = Staff.objects.all()
    context = {"Staff_data":staffs}
    return render(request,'about.html',context)

def contact(request):
    return render(request,'contact.html')