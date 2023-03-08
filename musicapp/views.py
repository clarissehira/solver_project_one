from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from musicapp.forms import RegisterUserForm
# Create your views here.
 
def login_user(request):
    if request.method == "POST":
        username=request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('welcome')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
            
    else:
        return render(request,'authenticate/login.html',{})
    
def logout_user(request):
    logout(request)
    messages.success(request,("you are loged out"))
    return redirect('welcome')

def legister_user(request):
    form = RegisterUserForm()
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            messages.success(request, "Registration successful")
            login(request, user)
            return redirect('login')
        else:
            messages.error(request, "Error: Invalid form submission")
    return render(request, 'authenticate/register.html', {'form': form})
