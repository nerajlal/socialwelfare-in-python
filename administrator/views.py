from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from account.models import register
from django.contrib.auth import authenticate, login
from oldage.models import *
from women.models import *
from orphanage.models import *
from user.models import *
from .models import *
# Create your views here.

def index(request):
    return render(request,'administrator/home.html')

def login(request):
    context = {
        'name': "n"
    }

    if request.method == 'POST':
        print("work post")
        username = request.POST['username']
        password = request.POST['password']
        if username != "" and password != "":
            user = authenticate(username=username, password=password)
            if user != None:
                # login(request, user)
                request.session["username"] = username
                return redirect(home)
            else:
                return render(request, 'administrator/signin.html', context)
        else:
            return render(request, 'administrator/signin.html', context)

    else:
        return render(request, 'administrator/signin.html', context)





def home(request):
    return render(request,'administrator/base.html')

def view_society(request):
    data=register.objects.filter(status=False)
    context={
        'data':data
    }
    return render(request,'administrator/view_society.html',context)

def approvejob(request):
    data=addjobdata.objects.all()
    context={
        'data':data
    }
    return render(request,'administrator/approvejob.html',context)

def showjob(request):
    data=approvedjob.objects.all()
    context={
        'data':data
    }
    return render(request,'showjob.html',context)

def showjobof(request):
    data=approvedjob.objects.all()
    context={
        'data':data
    }
    return render(request,'showjobof.html',context)


def approvedjobs(request,pk):
        obj=addjobdata.objects.get(pk=pk)
        create=approvedjob.objects.create(job=obj.job,description=obj.description,name=obj.name,address=obj.address,state=obj.state,phone=obj.phone,district=obj.district)
        create.save()
        obj5=addjobdata.objects.filter(pk=pk)
        obj5.delete()
        return redirect('/administrator/approvejob')

def removejob(request, pk):
        addjobdata.objects.filter(pk=pk).delete()
        
   
        return redirect('/administrator/approvejob')


def active_society(request, pk):
    register.objects.filter(pk=pk).update(status=True)
    data = register.objects.filter(status=False)
    context = {
        'data': data
    }

    return render(request, 'administrator/view_society.html', context)


def remove_society(request, pk):
    register.objects.filter(pk=pk).delete()
    data = register.objects.filter(status=False)
    context = {
        'data': data
    }

    return render(request, 'administrator/view_society.html', context)



# def view_oldage(request):
#     data=register.objects.filter(category="oldage",status=False)
#     context={
#         'data':data
#     }
#     return render(request,'administrator/view_oldage.html',context)


# def active_oldage(request, pk):
#     register.objects.filter(pk=pk).update(status=True)
#     data = register.objects.filter(status=False,category="oldage")

#     context = {
#         'data': data
#     }

#     return render(request, 'administrator/view_oldage.html', context)


# def remove_oldage(request, pk):
#     register.objects.filter(pk=pk).delete()
#     data = register.objects.filter(status=False,category="oldage")

#     context = {
#         'data': data
#     }

#     return render(request, 'administrator/view_oldage.html', context)


# def view_women_welfare(request):
#     data=register.objects.filter(category="women",status=False)
#     context={
#         'data':data
#     }
#     return render(request,'administrator/view_women_welfare.html',context)


# def active_women_welfare(request, pk):
#     register.objects.filter(pk=pk).update(status=True)
#     data = register.objects.filter(status=False,category="women")

#     context = {
#         'data': data
#     }

#     return render(request, 'administrator/view_women_welfare.html', context)


# def remove_women_welfare(request, pk):
#     register.objects.filter(pk=pk).delete()
#     data = register.objects.filter(status=False,category="women")

#     context = {
#         'data': data
#     }

#     return render(request, 'administrator/view_women_welfare.html', context)


def view_welfares(request):
    return render(request,'administrator/society.html')

def view_welfares_oldage(request):
    data = register.objects.filter(category="oldage",status=True)
    context = {
        'data': data
    }
    return render(request,'administrator/oldage.html',context)


def view_oldage_members(request,pk):
    data = oldage_members.objects.filter(oldage_id=pk)
    context = {
        'data': data
    }
    return render(request,'administrator/oldage_members.html',context) 



def view_welfares_women(request):
    data = register.objects.filter(category="women",status=True)
    context = {
        'data': data
    }
    return render(request,'administrator/women.html',context)



def view_women_members(request,pk):
    data = women_members.objects.filter(women_id=pk)
    context = {
        'data': data
    }
    return render(request,'administrator/women_member.html',context)  


def view_welfare_orphanage(request):
    data = register.objects.filter(category="orphanage",status=True)
    context = {
        'data': data
    }
    return render(request,'administrator/orphanage.html',context)

def view_orphanage_members(request,pk):
    data = orphanage_members.objects.filter(orphanage_id=pk)
    context = {
        'data': data
    }
    return render(request,'administrator/orphanage_members.html',context) 


def view_products(request):
    data = orphanage_product.objects.filter()
    data1=women_product.objects.filter()
    context = {
        'data': data,
        'data1':data1

    }
    return render(request,'administrator/products.html',context)


def view_purchase(request):
    data=women_purchase.objects.all()
    data1=orphanage_purchase.objects.all()
    context = {
        'data':data,
        "data1":data1
    }
    return render(request,'administrator/purchase.html',context)


def view_marriage_details(request):
    data=women_proposal.objects.all()
    context = {
        'data':data
    }
    return render(request,'administrator/marriage.html',context)   



def view_donation(request):
    data=women_donation.objects.all()
    data1=oldage_donation.objects.all()
    data2=orphanage_donation.objects.all()
    context = {
        'data':data,
        'data1':data1,
        'data2':data2
    }
    return render(request,'administrator/donation.html',context)   
