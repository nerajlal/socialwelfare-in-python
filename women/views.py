from atexit import register
from django.shortcuts import render,HttpResponse

from .models import *
from account.models import *
from administrator.models import *
# Create your views here.
def home(request):
    return render(request,'women_welfare/home.html')

def view_members(request):
    women_id=request.session['pid']
    data = women_members.objects.filter(women_id=women_id)
    context={
        'data':data
    }
    return render(request,'women_welfare/view_members.html',context)

def add_members(request):
    if request.method == 'POST':
        name=request.POST['name']
        dob=request.POST['dob']
        gender=request.POST['gender']
        status1=request.POST['status1']
        address=request.POST['address']
        district=request.POST['district']
        state=request.POST['state']
        pincode=request.POST['pincode']
        phone=request.POST['phone']
        account=request.POST['account']
        bank=request.POST['bank']  
        image=request.FILES['image']
        women_id=request.session['pid']
        user = women_members.objects.create(name=name,gender=gender,dob=dob,status1=status1,address=address,district=district,state=state,pincode=pincode,phone=phone,account=account,bank=bank,image=image,women_id=women_id)
        user.save()
        data = women_members.objects.filter(women_id=women_id)
        context={
            'data':data
        }
        return render(request,'women_welfare/view_members.html',context)

    return render(request,'women_welfare/add_members.html')

def edit_members(request,pk):
    if request.method == 'POST':
        
        try:
            name=request.POST['name']
            dob=request.POST['dob']
            status1=request.POST['status1']
            address=request.POST['address']
            district=request.POST['district']
            phone=request.POST['phone']
            account=request.POST['account']
            bank=request.POST['bank']  
            image=request.FILES['image']
                                                                                        
            user = women_members.objects.get(pk=pk)
            user.name = name
            user.dob = dob
            user.status1 = status1
            user.address = address
            user.district = district
            user.phone = phone
            user.account = account
            user.bank = bank
            user.image = image
            user.save()
            print(user)
            return HttpResponse('<script>alert("Updated Successfully");window.location="/women/view_members"</script>')
        except:
            name=request.POST['name']
            dob=request.POST['dob']
            status1=request.POST['status1']
            address=request.POST['address']
            district=request.POST['district']
            phone=request.POST['phone']
            account=request.POST['account']
            bank=request.POST['bank']  
                                                                                        
            user = women_members.objects.get(pk=pk)
            user.name = name
            user.dob = dob
            user.status1 = status1
            user.address = address
            user.district = district
            user.phone = phone
            user.account = account
            user.bank = bank
            
            user.save()
            print(user)
            return HttpResponse('<script>alert("Updated Successfully");window.location="/women/view_members"</script>')


    data = women_members.objects.get(id=pk)
    context = {
        'data': data,
    }
    return render(request,'women_welfare/edit_members.html',context)
def delete_members(request,pk):
    women_id=request.session['pid']
    women_members.objects.filter(pk=pk).delete()
    data = women_members.objects.filter(women_id=women_id)
    context = {
        'data': data
    }
    
    return render(request,'women_welfare/view_members.html',context)


def proposals(request):
    women_id=request.session['pid']
    welfare1=register.objects.get(pk=women_id)
    welfare=welfare1.society
    print(welfare)
    data=women_proposal.objects.filter(welfare=welfare)
    context={
        'data':data
    }
    return render(request,'women_welfare/proposal.html',context)

def products(request):
    women_id=request.session['pid']
    data=women_product.objects.filter(society_id=women_id)
    context={
        'data':data
    }
    return render(request,'women_welfare/products.html',context)

def add_products(request):
    if request.method == 'POST':
        pname=request.POST['pname']
        desc=request.POST['desc']
        price=request.POST['price']
        image=request.FILES['image']
        women_id=request.session['pid']
        women_id=request.session['pid']
        data=women_product.objects.filter(society_id=women_id)
        context={
            'data':data
        }
        
        product=women_product.objects.create(society_id=women_id,pname=pname,desc=desc,price=price,image=image)
        product.save()
        return render(request,'women_welfare/products.html',context)
    return render(request,'women_welfare/add_products.html')

def edit_products(request,pk):
    if request.method == 'POST':
        
            pname=request.POST['name']
            desc=request.POST['desc']
            price=request.POST['price']
            try:
                image=request.FILES['image']
            except:
                pass
            women_id=request.session['pid']
                                                                                        
            user = women_product.objects.get(pk=pk)
            user.pname = pname
            user.desc = desc
            user.price = price
            try:
                user.image = image
            except:
                pass
            user.society_id = women_id
            
            user.save()
            print(user)
            return HttpResponse('<script>alert("Updated Successfully");window.location="/women/products"</script>')
        


    data = women_product.objects.get(id=pk)
    context = {
        'data': data,
        'pk':pk
    }

    return render(request,'women_welfare/edit_product.html',context)

def delete_products(request,pk):
    women_id=request.session['pid']
    women_product.objects.filter(pk=pk).delete()
    data = women_product.objects.filter(society_id=women_id)
    context = {
        'data': data
    }
    return render(request,'women_welfare/products.html',context)

def purchase(request):
    women_id=request.session['pid']
    welfare1=register.objects.get(pk=women_id)
    welfare=welfare1.society
    data =women_purchase.objects.filter(society=welfare)
    context={
        'data':data
    }
    return render(request,'women_welfare/purchase.html',context)

def donations(request):
    women_id=request.session['pid']
    welfare1=register.objects.get(pk=women_id)
    welfare=welfare1.society
    data =women_donation.objects.filter(society=welfare)
    context={
        'data':data
    }
    return render(request,'women_welfare/donate.html',context)

def donation_received(request,pk):

    don_recieve=women_donation.objects.get(pk=pk)
    don_recieve.receive="Recieved"
    don_recieve.save()
    women_id=request.session['pid']
    welfare1=register.objects.get(pk=women_id)
    welfare=welfare1.society
    data =women_donation.objects.filter(society=welfare)
    context={
        'data':data
    }
    return render(request,'women_welfare/donate.html',context)

def showjob(request):
    data=approvedjob.objects.all()
    context={
        'data':data
    }
    return render(request,'women_welfare/showjob.html',context)

