from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.

def oldage_home(request):
    return render(request,'oldage/home.html')



def view_members(request):
    oldage_id=request.session['pid']
    data = oldage_members.objects.filter(oldage_id=oldage_id)
    context = {
        'data': data
    }
    return render(request,'oldage/view_members.html',context) 



def add_members(request):
    if request.method == 'POST':
        name=request.POST['name']
        gender=request.POST['gender']
        dob=request.POST['dob']
        address=request.POST['address']
        district=request.POST['district']
        state=request.POST['state']
        pincode=request.POST['pincode']
        phone=request.POST['phone']
        account=request.POST['account']
        image=request.FILES['image']
        oldage_id=request.session['pid']
        bank=request.POST['bank']                                                                                   
        user = oldage_members.objects.create(name=name,gender=gender,dob=dob,address=address,district=district,state=state,pincode=pincode,phone=phone,account=account,image=image,oldage_id=oldage_id,bank=bank)
        user.save()
        print(user)
        return HttpResponse('<script>alert("Added Successfully");window.location="/oldage/view_members"</script>')
    else:
        return render(request, 'oldage/add_members.html')

def edit_member_details(request,pk):
    data = oldage_members.objects.filter(id=pk)
    context = {
        'data': data,
    }
    return render(request, 'oldage/edit_members.html', context)


def edit_members(request,pk):
    try:
        name=request.POST['name']
        gender=request.POST['gender']
        dob=request.POST['dob']
        address=request.POST['address']
        district=request.POST['district']
        state=request.POST['state']
        pincode=request.POST['pincode']
        phone=request.POST['phone']
        account=request.POST['account']
        image=request.FILES['image']
        oldage_id=request.session['pid']
        bank=request.POST['bank']                                                                                   
        user = oldage_members.objects.get(pk=pk)
        user.name = name
        user.gender = gender
        user.dob = dob
        user.address = address
        user.district = district
        user.state = state
        user.pincode = pincode
        user.phone = phone
        user.account = account
        user.image = image
        user.oldage_id = oldage_id
        user.bank = bank
        user.save()
        print(user)
        return HttpResponse('<script>alert("Updated Successfully");window.location="/oldage/view_members"</script>')
    except:
        name=request.POST['name']
        gender=request.POST['gender']
        dob=request.POST['dob']
        address=request.POST['address']
        district=request.POST['district']
        state=request.POST['state']
        pincode=request.POST['pincode']
        phone=request.POST['phone']
        account=request.POST['account']
        oldage_id=request.session['pid']
        bank=request.POST['bank']                                                                                   
        user = oldage_members.objects.get(pk=pk)
        user.name = name
        user.gender = gender
        user.dob = dob
        user.address = address
        user.district = district
        user.state = state
        user.pincode = pincode
        user.phone = phone
        user.account = account
        user.oldage_id = oldage_id
        user.bank = bank
        user.save()
        print(user)
        return HttpResponse('<script>alert("Updated Successfully");window.location="/oldage/view_members"</script>')
    


def delete_member(request, pk):
    oldage_id=request.session['pid']
    oldage_members.objects.filter(pk=pk).delete()
    data = oldage_members.objects.filter(oldage_id=oldage_id)
    context = {
        'data': data
    }
    return render(request, 'oldage/view_members.html', context)


def view_donation(request):
    oldage_id=request.session['name']
    data = oldage_donation.objects.filter(society=oldage_id)
    context = {
        'data': data
    }
    return render(request,'oldage/view_donation.html',context) 


def receive(request, pk):
    oldage_id=request.session['name']
    oldage_donation.objects.filter(pk=pk).update(receive="Received")
    data = oldage_donation.objects.filter(society=oldage_id)

    context = {
        'data': data
    }

    return render(request, 'oldage/view_donation.html', context)
