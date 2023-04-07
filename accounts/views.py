# from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import PasswordChangeForm
# from . models import Crinfo,ReferralCode
from django.contrib.auth import update_session_auth_hash,logout
# from cr_portal.models import  Points
from django.contrib.auth import views as auth_views

from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm , UserUpdateForm , UserProfileUpdateForm

PATH = [""]

PREV_PATH = [""]

def signup(request,previous_path):
    if PREV_PATH[0] == "":
        PREV_PATH[0] = previous_path
    if request.method=='POST':

        
        name=request.POST['first_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if name=="" or  username=='' or email=='' or password1 ==''or password2=="":
            messages.info(request,"fill all the details to sign up")
            return redirect(f'/accounts/signup/suggestions/{PREV_PATH[0]}')
        elif not email.endswith("@gmail.com"):
            messages.info(request,"invalid gmail")
            return redirect(f'/accounts/signup/suggestions/{PREV_PATH[0]}')
        
        else:
            if password1==password2:


                if User.objects.filter(username=username).exists():

                    messages.info(request,"user already exists")
                    return redirect(f'/accounts/signup/suggestions/{PREV_PATH[0]}')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,"email already exists")
                    return redirect(f'/accounts/signup/suggestions/{PREV_PATH[0]}')

                else:

                    user=User.objects.create_user(first_name=name,email=email,username=username,password=password1)
                    user.save();
                    messages.info(request,"user created")
                    redirect_url = f'/accounts/login/suggestions/{PREV_PATH[0]}'
                    PREV_PATH[0] = ""
                    return redirect(redirect_url)
                   

            else:

                messages.info(request,"password not matching..")

                return redirect(f'/accounts/signup/suggestions/{PREV_PATH[0]}')

    else:

        return render(request,'signup.html')

def login(request,prev_path):
    # print(PATH[0])
    if PATH[0] == "":
        PATH[0] = prev_path
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
        #     authenticated = {
        #     "bool" : "True"
        # }
            redirect_url = f'/suggestions/{PATH[0]}'
            PATH[0] = ""
            return redirect(redirect_url)
        else:
            messages.info(request,'authentication failed')
            return redirect(f'/accounts/login/suggestions/{PATH[0]}',{'prev_path':prev_path})
    else:
        return render(request,'login.html',{'prev_path':prev_path})

@login_required
def Profile(request):
    user=request.user
    if request.method == 'POST':
        u_form= UserUpdateForm(request.POST, instance=request.user)
        p_form=UserProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'your account has been updated!')
            return redirect('profile')
    else:
        u_form= UserUpdateForm(request.POST, instance=request.user)
        p_form= UserProfileUpdateForm(request.POST, instance=request.user.profile)
    context={
        'u_form':u_form,
        'p_form':p_form,
        'img_url':user.profile.image.url
    }
    return render(request,'profile.html',context)

def logout_view(request,prev):
    logout(request)
    redirect_url = f'/suggestions/{prev}'
    return redirect(redirect_url)
