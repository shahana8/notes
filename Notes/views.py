from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import sampleNote
from .forms import noteForm

@login_required(login_url='login')
def myNote(request):
    mynote = sampleNote.objects.all()
    context = {'note': mynote}
    return render(request, 'Notes/frontpage.html', context)

def singleNote(request, pk):
    mynote = sampleNote.objects.get(id=pk)
    context = {'note': mynote}
    return render(request, 'Notes/viewpage.html', context)

@login_required(login_url='login')
def createNote(request):
    form = noteForm()


    if request.method == 'POST':
        form = noteForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.owner = request.user
            user.save()
            return redirect('frontpage')

    context = {'form': form}
    return render(request, 'Notes/addupdate_form.html', context)


def updateNote(request, pk):
    note = sampleNote.objects.get(id=pk)
    form = noteForm(instance=note)

    if note.owner != request.user:
        return redirect('frontpage')


    if request.method == 'POST':
        form = noteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('frontpage')

    context = {'form': form}
    return render(request, 'Notes/addupdate_form.html', context)

def deleteNote(request, pk):
    note = sampleNote.objects.get(id=pk)
    if note.owner != request.user:
        return redirect('frontpage')
    note.delete()
    return redirect('frontpage')

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('frontpage')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'username does not exist')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('frontpage')

        else:

            messages.error(request, 'username or password is incorrect')

    return render(request, 'Notes/login_register.html', {'page':page})

def logoutUser(request):
    logout(request)
    messages.info(request,'user logged out')
    return redirect('login')
def registerUser(request):
    page = 'register'

    form = UserCreationForm()

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Registered successfully')

            login(request, user)
            return redirect('frontpage')

        else:

            messages.error(request, 'error occurred during registration')

    context = {'page':page, 'form':form}
    return render(request, 'Notes/login_register.html', context)

# Create your views here.
