from django.shortcuts import render,HttpResponse
from .models import *
from administrator.models import *
# Create your views here.

def showjob(request):
    data=approvedjob.objects.all()
    context={
        'data':data
    }
    return render(request,'orphanage/showjob.html',context)
def orphanage_home(request):
    return render(request,'orphanage/home.html')

def view_members(request):
    orphan=request.session['pid']
    data = orphanage_members.objects.filter(orphanage_id=orphan)
    context = {
        'data': data
    }
    return render(request,'orphanage/members.html',context)


def add_members(request):
    if request.method == 'POST':
        name=request.POST['name']
        gender=request.POST['gender']
        age=request.POST['age']
        talent=request.POST['talent']
        disability=request.POST['disability']
        state=request.POST['state']
        account=request.POST['account']
        image=request.FILES['image']
        orphan_id=request.session['pid']
        bank=request.POST['bank']                                                                                   
        user = orphanage_members.objects.create(name=name,gender=gender,age=age,talent=talent,disability=disability,state=state,account=account,bank=bank,image=image,orphanage_id=orphan_id)
        user.save()
        print(user)
        return HttpResponse('<script>alert("Added Successfully");window.location="/orphanage/view_members"</script>')
    else:
        return render(request, 'orphanage/add_members.html')


def edit_member(request,pk):
    data = orphanage_members.objects.filter(id=pk)
    context = {
        'data': data,
    }
    return render(request, 'orphanage/edit_member.html', context)


def edit_member1(request,pk):
    try:
        name=request.POST['name']
        gender=request.POST['gender']
        age=request.POST['age']
        talent=request.POST['talent']
        disability=request.POST['disability']
        state=request.POST['state']
        account=request.POST['account']
        image=request.FILES['image']
        orphan_id=request.session['pid']
        bank=request.POST['bank']                                                                                   
        user = orphanage_members.objects.get(pk=pk)
        user.name = name
        user.gender = gender
        user.age = age
        user.talent = talent
        user.disability = disability
        user.state = state
        user.account = account
        user.image = image
        user.oldage_id = orphan_id
        user.bank = bank
        user.save()
        print(user)
        return HttpResponse('<script>alert("Updated Successfully");window.location="/orphanage/view_members"</script>')
    except:
        name=request.POST['name']
        gender=request.POST['gender']
        age=request.POST['age']
        talent=request.POST['talent']
        disability=request.POST['disability']
        state=request.POST['state']
        account=request.POST['account']
        orphan_id=request.session['pid']
        bank=request.POST['bank']                                                                                  
        user = orphanage_members.objects.get(pk=pk)
        user.name = name
        user.gender = gender
        user.age = age
        user.talent = talent
        user.disability = disability
        user.state = state
        user.account = account
        user.oldage_id = orphan_id
        user.bank = bank
        user.save()
        print(user)
        return HttpResponse('<script>alert("Updated Successfully");window.location="/orphanage/view_members"</script>')
    

def delete_member(request, pk):
    orphanage_id=request.session['pid']
    orphanage_members.objects.filter(pk=pk).delete()
    data = orphanage_members.objects.filter(orphanage_id=orphanage_id)
    context = {
        'data': data
    }
    return render(request, 'orphanage/members.html', context)



def view_products(request):
    orphanage_id=request.session['pid']
    data = orphanage_product.objects.filter(society_id=orphanage_id)
    context = {
        'data': data
    }
    return render(request,'orphanage/products.html',context) 


def add_products(request):
    if request.method == 'POST':
        orphan_id=request.session['pid']
        pname=request.POST['pname']
        desc=request.POST['desc']
        price=request.POST['price']
        image=request.FILES['image']
                                                                                         
        user = orphanage_product.objects.create(society_id=orphan_id,pname=pname,desc=desc,price=price,image=image)
        user.save()
        print(user)
        return HttpResponse('<script>alert("Added Successfully");window.location="/orphanage/view_products"</script>')
    else:
        return render(request, 'orphanage/add_products.html')



def edit_product(request,pk):
    data = orphanage_product.objects.filter(id=pk)
    context = {
        'data': data,
    }
    return render(request, 'orphanage/edit_product.html', context)


def edit_product1(request,pk):
    try:
        orphan_id=request.session['pid']
        pname=request.POST['pname']
        desc=request.POST['desc']
        price=request.POST['price']
        image=request.FILES['image']                                                                                 
        user = orphanage_product.objects.get(pk=pk)
        user.name = pname
        user.pname = pname
        user.desc = desc
        user.society_id = orphan_id
        user.price = price
        user.image = image
        user.save()
        print(user)
        return HttpResponse('<script>alert("Updated Successfully");window.location="/orphanage/view_products"</script>')
    except:
        orphan_id=request.session['pid']
        pname=request.POST['pname']
        desc=request.POST['desc']
        price=request.POST['price']                                                                               
        user = orphanage_product.objects.get(pk=pk)
        user.name = pname
        user.pname = pname
        user.desc = desc
        user.society_id = orphan_id
        user.price = price
        user.save()   
        print(user)
        return HttpResponse('<script>alert("Updated Successfully");window.location="/orphanage/view_products"</script>')
    

def delete_product(request, pk):
    orphanage_id=request.session['pid']
    orphanage_product.objects.filter(pk=pk).delete()
    data = orphanage_product.objects.filter(society_id=orphanage_id)
    context = {
        'data': data
    }
    return render(request, 'orphanage/products.html', context)


def view_purchase(request):
    orphanage_id=request.session['name']
    data = orphanage_purchase.objects.filter(society=orphanage_id)
    context = {
        'data': data
    }
    return render(request,'orphanage/view_purchase.html',context) 


def view_adoption(request):
    orphanage_id=request.session['name']
    data = orphanage_adoption.objects.filter(society=orphanage_id)
    context = {
        'data': data
    }
    return render(request,'orphanage/view_adoption.html',context) 


def view_sponsor(request):
    orphanage_id=request.session['name']
    data = orphanage_sponsor.objects.filter(society=orphanage_id)
    context = {
        'data': data
    }
    return render(request,'orphanage/view_sponsor.html',context) 



def view_donation(request):
    orphanage_id=request.session['name']
    data = orphanage_donation.objects.filter(society=orphanage_id)
    context = {
        'data': data
    }
    return render(request,'orphanage/view_donation.html',context) 


def receive(request, pk):
    orphanage_id=request.session['name']
    orphanage_donation.objects.filter(pk=pk).update(receive="Received")
    data = orphanage_donation.objects.filter(society=orphanage_id)
    context = {
        'data': data
    }
    return render(request, 'orphanage/view_donation.html', context)