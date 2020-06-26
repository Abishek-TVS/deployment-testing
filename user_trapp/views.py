from django.shortcuts import render
from user_trapp.forms import User_form, UserProfile_Form

from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):    
    return render(request, 'index.html')

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index1'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request,username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return render(request, 'welcomepage.html', {'name':request.POST['username']})
            else:
                return HttpResponse('User is not active')
        else:
            return HttpResponse('someone tried to login')
    
    return render(request, 'login.html')

    
def register(request):
    registered = False
    
    if request.method == 'POST':
        userForm = User_form(data=request.POST)
        userProfileForm = UserProfile_Form(data=request.POST)

        if userForm.is_valid() and userProfileForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()

            profile = userProfileForm.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                print(request.FILES)
            print(request.FILES)
            profile.save()

            registered = True
        else:
            print(userForm.errors,userProfileForm.errors)
    
    else:
        userForm = User_form()
        userProfileForm = UserProfile_Form()
    
    return render(request, 'register.html',
                                {'User_form':userForm,
                                'UserProfile_Form':userProfileForm,
                                'registered' :registered})
