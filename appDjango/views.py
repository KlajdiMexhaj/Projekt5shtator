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
    if request.method == "POST":
       a = request.POST["emri"]
       mbiemri_ = request.POST["mbiemri"]
       email_ = request.POST["email"]
       sms_ = request.POST["sms"]

        #    ruajtja ne databaze
       Contact(
            contact_name = a,
            contact_mbiemri = mbiemri_,
            contact_email = email_,
            contact_sms = sms_,
        ).save()
    return render(request,'contact.html')

def itemDetail(request,id):
    item_detail = Item.objects.get(item_id=id)
    
    context = {"item_detail":item_detail}
    return render(request,"itemDetail.html",context)

def itemCategory(request,id):
    item_category = Kategori.objects.get(pk=id)
    category_items = Item.objects.filter(item_category=item_category)
    context = {"item_category":item_category, 'category_items':category_items}
    return render(request,"itemCategory.html",context)