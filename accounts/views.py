from django.shortcuts import render,redirect
from django.conf import settings
from .forms import SignUpForm,LoginForm,EditProfileForm,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from .models import CostomUser
from home.models import Post
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy

def SignUpView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            CostomUser.objects.create_user(cd['username'],cd['email'],cd['password'])
            messages.success(request,'Please fill this form','success')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})
    
def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],email=cd['email'],password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,'You logged in successfully','success')
                return redirect('home')
            else:
                messages.error(request,'username or email or password is wrong','danger')
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})

def LogoutView(request):
    logout(request)
    messages.success(request,'You logged out successfully','success')
    return redirect('home')

def ProfileView(request):
    profile = request.user
    posts = Post.objects.filter(author=profile)
    return render(request,'profile.html',{'profile':profile,'posts':posts})

def ProfileEdit(request):
    profile = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form= EditProfileForm(instance=profile)
    return render(request,'profile_edit.html',{"form":form})

class PasswordChangeView(auth_views.PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'registration/password_change_form.html'
