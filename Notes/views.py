from django.shortcuts import render, redirect
from .models import sampleNote
from .forms import noteForm

def myNote(request):
    mynote = sampleNote.objects.all()
    context = {'note': mynote}
    return render(request, 'Notes/frontpage.html', context)

def singleNote(request, pk):
    mynote = sampleNote.objects.get(id=pk)
    context = {'note': mynote}
    return render(request, 'Notes/viewpage.html', context)

def createNote(request):
    form = noteForm()

    if request.method == 'POST':
        form = noteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('frontpage')

    context = {'form': form}
    return render(request, 'Notes/addupdate_form.html', context)

def updateNote(request, pk):
    note = sampleNote.objects.get(id=pk)
    form = noteForm(instance=note)

    if request.method == 'POST':
        form = noteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('frontpage')

    context = {'form': form}
    return render(request, 'Notes/addupdate_form.html', context)

def deleteNote(request, pk):
    note = sampleNote.objects.get(id=pk)
    note.delete()
    return redirect('frontpage')


# Create your views here.
