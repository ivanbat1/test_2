from django.shortcuts import render
from .forms import *
from django.contrib import auth
# Create your views here.
def note(request):
    username = auth.get_user(request).username
    note = Note.objects.filter(user__username=username).order_by('note')
    form = NoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'note.html', locals())
    return render(request, 'note.html', locals())
