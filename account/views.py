
from django.contrib import messages
from django.shortcuts import redirect, render,HttpResponse
from .models import *
# Create your views here.

def home(request):
    return render(request,'indexa.html')

def register1(request):
    if request.method == 'POST':
        category=request.POST['category']
        society=request.POST['society']
        manager=request.POST['manager']
        address=request.POST['address']
        district=request.POST['city']
        state=request.POST['state']
        pincode=request.POST['pincode']
        phone=request.POST['phone']
        acc_no=request.POST['acc_no']
        bank_details=request.POST['bank_details']
        email=request.POST['email']                                                                                     
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password == cpassword:
            if register.objects.filter(email=email).exists():
                messages.info(request, "Username already exists")
                return HttpResponse('<script>alert("Username Exists");window.location="register"</script>')
            else:
                user = register.objects.create(category=category,society=society,manager=manager,address=address,district=district,state=state,pincode=pincode,phone=phone,account=acc_no,bank=bank_details,email=email,password=password)
                user.save()
                print(user)
                return render(request, 'signup.html')
        else:
            print("Password doesnot match")
            return HttpResponse('<script>alert("Password doesnot match");window.location="register1"</script>')

    else:
        return render(request, 'signup.html')


def login(request):
    try:
        if request.method == "POST":
            email = request.POST['username']
            password = request.POST['password']
            ob = register.objects.get(email=email, password=password)
            
            # print(ob)

            if ob is not None:
                print("ob found")
                request.session['lg'] = 'lin'
                user_name = ob.society
                request.session['name'] = user_name
                request.session['lid'] = ob.email
                request.session['pid']=ob.pk
                print(request.session['pid'])
                request.session['lg'] = 'true'
                if ob.category == "orphanage":
                    active = register.objects.get(email=email)
                    # print("doctor active", active.approve)
                    if active.status == True:
                        return  redirect('/orphanage/')
                elif ob.category == "oldage":
                    return redirect('/oldage/')
                elif ob.category == "women":
                    return render(request, "women_welfare/home.html")
                else:
                    return render(request, "user/home.html")
                    # return render(request, "View_Quiz_List.html", {'data': user_name})
            else:
                return HttpResponse('<script>alert("Invalid Password");window.location="login"</script>')
        else:
            print("Post not working")
            return render(request, 'signin.html')
    except Exception as e:
        messages.info(request, 'Invalid Username or Password')
        return HttpResponse('<script>alert("Invalid Password");window.location=""</script>')
    return render(request, 'login/login.html')



def signout(request):
    return render(request,"indexa.html")