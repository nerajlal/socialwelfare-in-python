from django.shortcuts import render
from .models import addjobdata
from oldage.models import *
from orphanage.models import *
from women.models import *
from account.models import *
# Create your views here.
def index(request):
    return render(request,'user/home.html')

def viewaddjob(request):
    return render(request,'user/addjob.html')

def addjob(request):

    if request.method == 'POST':
        job=request.POST['job']
        description=request.POST['description']
        name=request.POST['name']
        address=request.POST['address']
        state=request.POST['state']
        phone=request.POST['phone']
        district=request.POST['district']

        purchase = addjobdata.objects.create(job=job,description=description,name=name,address=address,state=state,phone=phone,district=district)
        purchase.save()

    #     data = women_product.objects.all()
    #     context={
    #         'data':data
    #     }

    #     return render(request,'user/purchase_women.html',context)


    # context={
    #     'pk':pk
    # }
    return render(request,'user/addjob.html')

def societies(request):
    return render(request,'user/societies.html')

def societies_oldage(request):
    data = register.objects.filter(category="oldage",status=True)
    context={
        'data':data
    }
    return render(request,'user/societies_oldage.html',context)
def societies_oldage_member(request,pk):
    data = oldage_members.objects.filter(oldage_id=pk)
    context={
        'data':data
    }
    return render(request,'user/societies_oldage_member.html',context)

def societies_oldage_donate(request,pk):
    if request.method == 'POST':
        name=request.POST['name']
        address=request.POST['address']
        district=request.POST['district']
        state=request.POST['state']
        phone=request.POST['phone']
        amount=request.POST['amount']
        society1=register.objects.get(pk=pk)
        society2=society1.society
        receive="Not Recieved"
        

        donation = oldage_donation.objects.create(name=name,address=address,state=state,phone=phone,amount=amount,receive=receive,district=district,society=society2)
        donation.save()
        data = register.objects.filter(category="oldage",status=True)
        context={
            'data':data
        }
        return render(request,'user/societies_oldage.html',context)
    context={
        'pk':pk
    }
    return render(request,'user/societies_oldage_donate.html',context)

def societies_women(request):
    data = register.objects.filter(category="women",status=True)
    context={
        'data':data
    }
    return render(request,'user/societies_women.html',context)
    

def societies_women_member(request,pk):
    data = women_members.objects.filter(women_id=pk)
    context={
        'data':data
    }
    

    return render(request,'user/societies_women_member.html',context)

def societies_women_donate(request,pk):
    if request.method == 'POST':
        name=request.POST['name']
        address=request.POST['address']
        district=request.POST['district']
        state=request.POST['state']
        phone=request.POST['phone']
        amount=request.POST['amount']
        society1=register.objects.get(pk=pk)
        society2=society1.society
        receive="Not Recieved"
        

        donation = women_donation.objects.create(name=name,address=address,state=state,phone=phone,amount=amount,receive=receive,district=district,society=society2)
        donation.save()
        data = register.objects.filter(category="women",status=True)
        context={
            'data':data
        }
        return render(request,'user/societies_women.html',context)
    context={
        'pk':pk
    }
    
    return render(request,'user/societies_women_donate.html',context)

def societies_orphanage(request):
    data = register.objects.filter(category="orphanage",status=True)
    context={
        'data':data
    }
    return render(request,'user/societies_orphanage.html',context)

def societies_orphanage_member(request,pk):
    data = orphanage_members.objects.filter(orphanage_id=pk)
    context={
        'data':data
    }
    
    return render(request,'user/societies_orphanage_member.html',context)

def societies_orphanage_donate(request,pk):
    if request.method == 'POST':
        name=request.POST['name']
        address=request.POST['address']
        district=request.POST['district']
        state=request.POST['state']
        phone=request.POST['phone']
        amount=request.POST['amount']
        society1=register.objects.get(pk=pk)
        society2=society1.society
        receive="Not Recieved"
        

        donation = orphanage_donation.objects.create(name=name,address=address,state=state,phone=phone,amount=amount,receive=receive,district=district,society=society2)
        donation.save()
        data = register.objects.filter(category="orphanage",status=True)
        context={
            'data':data
        }
        return render(request,'user/societies_orphanage.html',context)
    context={
        'pk':pk
    }
    return render(request,'user/societies_orphanage_donate.html',context)

def adoption(request):
    return render(request,'user/adoption.html')

def adoption_members(request):
    data = register.objects.filter(category="orphanage",status=True)
    context={
        'data':data
    }
    
    return render(request,'user/adoption_members.html',context)


def adoption_member_detail(request,pk):
    data = orphanage_members.objects.filter(orphanage_id=pk)
    context={
        'data':data
    }
    
    
    return render(request,'user/adoption_member_detail.html',context)

def adoption_member_adopt(request,pk):

    if request.method == 'POST':
        name=request.POST['name']
        marital=request.POST['marital']
        designation=request.POST['desig']
        address=request.POST['address']
        district=request.POST['district']
        state=request.POST['state']
        phone=request.POST['phone']
        email=request.POST['email']
        reason=request.POST['reason']
        soc=orphanage_members.objects.get(pk=pk)
        soc1=soc.orphanage_id
        soc2=register.objects.get(pk=soc1)
        soc3=soc2.society
        adoption = orphanage_adoption.objects.create(child_id=pk,name=name,marital=marital,designation=designation,address=address,district=district,state=state,phone=phone,email=email,reason=reason,society=soc3)
        adoption.save()

        return render(request,'user/adoption_success.html')
    context={
        'pk':pk
    }
    return render(request,'user/adoption_member_adopt.html',context)

def sponsorship(request):
    return render(request,'user/sponsorship.html')
def sponsorship_members(request):
    data = register.objects.filter(category="orphanage",status=True)
    context={
        'data':data
    }
    return render(request,'user/sponsorship_members.html',context)
def sponsorship_member_detail(request,pk):
    data = orphanage_members.objects.filter(orphanage_id=pk)
    context={
        'data':data
    }

    return render(request,'user/sponsorship_member_detail.html',context)

def sponsorship_member_sponsor(request,pk):
    if request.method == 'POST':
        name=request.POST['name']
        marital=request.POST['marital']
        designation=request.POST['desig']
        address=request.POST['address']
        district=request.POST['district']
        state=request.POST['state']
        phone=request.POST['phone']
        email=request.POST['email']
        soc=orphanage_members.objects.get(pk=pk)
        soc1=soc.orphanage_id
        soc2=register.objects.get(pk=soc1)
        soc3=soc2.society
        sponsorship = orphanage_sponsor.objects.create(child_id=pk,name=name,marital=marital,designation=designation,address=address,district=district,state=state,phone=phone,email=email,society=soc3)
        sponsorship.save()

        return render(request,'user/sponsorship_success.html')
    context={
        'pk':pk
    }
    return render(request,'user/sponsorship_member_sponsor.html',context)

def wedding(request):
    return render(request,'user/wedding.html')

def wedding_welfares(request):
    data = register.objects.filter(category="women",status=True)
    context={
        'data':data
    }
    return render(request,'user/wedding_welfares.html',context)

def wedding_member_detail(request,pk):
    data = women_members.objects.filter(women_id=pk,status1='single')
    context={
        'data':data
    }

    return render(request,'user/wedding_member_detail.html',context)

def wedding_member_propose(request,pk):
    if request.method == 'POST':
        name=request.POST['name']
        dob=request.POST['dob']
        occupation=request.POST['occupation']
        address=request.POST['address']
        district=request.POST['district']
        state=request.POST['state']
        phone=request.POST['phone']
        image=request.FILES['file1']
        women1=women_members.objects.get(pk=pk)
        women=women1.name
        welfare_id=women1.women_id
        society1=register.objects.get(pk=welfare_id)
        society2=society1.society
        propose = women_proposal.objects.create(name=name,dob=dob,occupation=occupation,address=address,district=district,state=state,phone=phone,image=image,women=women,welfare=society2)
        propose.save()

        return render(request,'user/proposal_success.html')

    context={
        'pk':pk
    }
    return render(request,'user/wedding_member_propose.html',context)

def purchase(request):
    data = women_product.objects.all()
    context={
        'data':data
    }

    return render(request,'user/purchase_women.html',context)

def purchase_buy(request,pk):

    if request.method == 'POST':
        name=request.POST['name']
        address=request.POST['address']
        state=request.POST['state']
        phone=request.POST['phone']
        district=request.POST['district']
        item1=women_product.objects.get(pk=pk)
        item=item1.pname
        sid=item1.society_id
        society1=register.objects.get(pk=sid)
        society2=society1.society
        purchase = women_purchase.objects.create(name=name,address=address,state=state,phone=phone,item=item,district=district,society=society2)
        purchase.save()

        data = women_product.objects.all()
        context={
            'data':data
        }

        return render(request,'user/purchase_women.html',context)


    context={
        'pk':pk
    }
    return render(request,'user/purchase_buy.html',context)

def purchase_orphanage(request):
    data = orphanage_product.objects.all()
    context={
        'data':data
    }

    return render(request,'user/purchase_orphanage.html',context)

def purchase_orphanage_buy(request,pk):

    if request.method == 'POST':
        print("Entering Successfully")
        name=request.POST['name']
        address=request.POST['address']
        state=request.POST['state']
        phone=request.POST['phone']
        district=request.POST['district']
        item1=orphanage_product.objects.get(pk=pk)
        item=item1.pname
        sid=item1.society_id
        society1=register.objects.get(pk=sid)
        society2=society1.society
        purchase = orphanage_purchase.objects.create(name=name,address=address,state=state,phone=phone,item=item,district=district,society=society2)
        purchase.save()

        data = orphanage_product.objects.all()
        context={
            'data':data
        }

        return render(request,'user/purchase_orphanage.html',context)
    context={
        'pk':pk
    }
    return render(request,'user/purchase_orphanage_buy.html',context)