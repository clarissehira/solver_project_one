from django.shortcuts import render,redirect
from website.forms import MusicianForm
from . models import Musician
from django.contrib import messages

# Create your views here.
def welcome(request):
   all_musicians= Musician.objects.all()
   return render(request,'index.html',{'all':all_musicians})

def inmusician(request):
    all_musicians= Musician.objects.all()
    return render(request,'in.html',{'all':all_musicians})


def join(request):
    if request.method == "POST":
        form = MusicianForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,'your form has been submitted')
            print('Data saved to database')
            #return render(request, 'index.html', {})
            return redirect(welcome)
        else:
            # Add this line to print out the error messages
            print(form.errors)
            return render(request, 'join.html', {'form': form})
    else:
        form = MusicianForm()
    return render(request, 'join.html', {'form': form})
