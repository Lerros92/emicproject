from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from .models import Note, Item
# Create your views here.

def index(request):
    return HttpResponse("Hello world")

class NoteListView(generic.ListView):
    model = Note