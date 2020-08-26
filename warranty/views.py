from django.shortcuts import render, redirect
from django import forms
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Note, Item, ItemLog
from .forms import NoteCreateForm, ItemAddForm, NoteUpdateForm, ItemUpdateForm, LogCreateForm
# Create your views here.

#Replace default DateInput


#<---------------View for project--------------->
#index
def index(request):
    return HttpResponse("Hello world")

class NoteListView(generic.ListView):
    model = Note

class ItemListView(generic.ListView):
    model = Item

#<-------------------Note Views------------------->
#CREATE
def CreateNote(request):
    if request.method == 'POST':
        form = NoteCreateForm(request.POST)
        if form.is_valid():
            add_Note = Note()
            add_Note.noteNumber = form.cleaned_data['noteNumber']
            add_Note.customers = form.cleaned_data['customers']
            add_Note.customersObj = form.cleaned_data['customersObj']
            add_Note.receiveDay = form.cleaned_data['receiveDay']
            add_Note.note = form.cleaned_data['note']
            add_Note.numOrder = Note.objects.all().count() + 1
            add_Note.save()
            return redirect('warranty:notes')
        else:
            return HttpResponse('Dữ liệu nhập vào không hợp lệ')
    else:
        form = NoteCreateForm()
        return render(request, 'warranty/note_create.html', {'form': form})

class NoteCreate(CreateView):
    # form_class = NoteForm
    model = Note
    form_class = NoteCreateForm
    template_name = 'warranty/note_create.html'
    success_url = reverse_lazy('warranty:notes')

#READ

def NoteDetail(request, pk):
    if request.method == 'POST':
        pass
    else:
        try:
            note_detail = Note.objects.get(id=int(pk))
        except:
            return HttpResponse('Không có số phiếu này')
        context = {
            'note_detail': note_detail,
            'items': note_detail.item.all(),
            'form': ItemAddForm
        }
        return render(request, 'warranty/note_detail.html', context)

#UPDATE
class NoteUpdate(UpdateView):
    model = Note
    form_class = NoteUpdateForm
    template_name = 'warranty/note_update.html'
    # success_url = reverse_lazy('warranty:notes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['noteNumber']=self.object.noteNumber
        return context

    def get_success_url(self, **kwargs):         
        return reverse_lazy("warranty:note_detail", args=(self.object.id,))

#DELETE
class NoteDelete(DeleteView):
    model = Note
    template_name = "warranty/note_delete.html"
    success_url = "warranty:notes"


#<-------------------Item Views------------------->
#CREATE
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
            return redirect('warranty:note_detail', pk=add_item.noteNumber.id)
        else:
            return HttpResponse("Form is not valid")
    else:
        form = ItemAddForm()
        return render(request, 'warranty/additem_page.html', {'form':form})

#READ
class ItemDetailView(generic.DetailView):
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ItemLogs']=self.object.log.all()
        return context

#UPDATE
class ItemUpdate(generic.UpdateView):
    model = Item
    form_class = ItemUpdateForm
    template_name = 'warranty/item_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['noteNumber']=self.object.noteNumber
        return context

    def get_success_url(self, **kwargs):         
        return reverse_lazy("warranty:note_detail", args=(self.object.noteNumber.id,))

class ItemDelete(DeleteView):
    model = Item
    template_name = "warranty/item_delete.html"
    success_url = "warranty:items"

#<-------------------ItemLog Views------------------->
#Item log Create:

def LogCreate(request):
    if request.method == 'POST':
        form = LogCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('warranty:item_detail', pk = form.cleaned_data["item"].id)
        else:
            return HttpResponse('Invalid form')


class ItemLogDelete(DeleteView):
    model = ItemLog
    template_name = "warranty/log_delete.html"
    
    def get_success_url(self, **kwargs):         
        return reverse_lazy("warranty:item_detail", args=(self.object.item.id,))


# <------------------Test function------------------>
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
        