from django.shortcuts import render, redirect
from django import forms
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Note, Item
from .forms import NoteCreateForm, ItemAddForm, NoteUpdateForm, ItemUpdateForm
from .forms import DateInput
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
    form_class = NoteCreateForm
    template_name = 'warranty/note_create.html'
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

class ItemDetailView(generic.DetailView):
    model = Item