from django.shortcuts import render
from login.forms import UserForm,UserprofileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def index(request):
    return render(request,'login/index.html')


@login_required
def special(request):
    return HttpResponse("You are loged In")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):

    registered=False

    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profileform=UserprofileInfoForm(data=request.POST)

        if user_form.is_valid() and profileform.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profileform.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()
            registered=True

        else:
            print(user_form.errors,profileform.errors)

    else:
        user_form=UserForm()
        profileform=UserprofileInfoForm()

    return render(request,'login/registration.html',
                            {'user_form':user_form,
                             'profileform':profileform,
                             'registered':registered})


def user_login(request):
    if request.method=='POST':
        username=request.POST.get('txtUsername')
        password=request.POST.get('txtPassword')
        print(username)
        user=authenticate(username=username,password=password)

        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not active")

        else:
            print("Some one try to login")
            print("Usrname:{} and Password{}".format(username,password))
            return HttpResponse("Invalid Login Detail")

    else:
        # return render(request,'login/index.html')
        return render(request,"login/login.html",{})
