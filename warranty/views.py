from django.shortcuts import render, redirect
from django import forms
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Note, Item
from .forms import NoteForm, ItemAddForm
# Create your views here.

#Replace default DateInput


#<---------------View for project--------------->
def index(request):
    return HttpResponse("Hello world")

class NoteListView(generic.ListView):
    model = Note

class ItemListView(generic.ListView):
    model = Item

class NoteCreate(CreateView):
    # form_class = NoteForm
    model = Note
    fields = '__all__'
    labels = {
        'noteNumber': 'Số phiếu xuất:',
        'customers': 'Tên khách hàng:',
        'receiveDay': 'Ngày tiếp nhận',
        'note': 'Ghi chú',
    }
    # widgets = {
    #     'receiveDay': forms.DateInput,
    # }
    success_url = reverse_lazy('warranty:notes')

def AddNote(request):    
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('warranty:notes')
        else:
            return render(request,'warranty/addnote_page.html',{'form':form})
    else:
        form = NoteForm()
        return render(request,'warranty/addnote_page.html',{'form':form})

def NoteDetail(request, pk):
    pass

class ItemUpdate(generic.UpdateView):
    model = Item
    exclude = ['noteNumber']

def AddItem(request):
    if request.method == 'POST':
        form = ItemAddForm(request.POST)
        # form.noteNumber = int(request.POST['noteNumber'])
        if form.is_valid():
            add_item = Item()
            add_item.noteNumber = Note.objects.get(pk=int(request.POST['noteNumber']))
            add_item.itemName = form.cleaned_data['itemName']
            add_item.quantity = form.cleaned_data['quantity']
            add_item.itemGroup = form.cleaned_data['itemGroup']
            add_item.status = form.cleaned_data['status']
            add_item.check = form.cleaned_data['check']
            add_item.conclude = form.cleaned_data['conclude']
            add_item.deadline = form.cleaned_data['deadline']
            add_item.note = form.cleaned_data['note']
            add_item.done = form.cleaned_data['done']
            add_item.save()
            return redirect('warranty:items')
        else:
            return HttpResponse("Form is not valid")
    else:
        form = ItemAddForm()
        return render(request, 'warranty/additem_page.html', {'form':form})