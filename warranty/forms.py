from django import forms
from .models import Note, Item, ItemLog

class DateInput(forms.DateInput):
    input_type = 'date'

class NoteCreateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        widgets = {
        'receiveDay': DateInput(),
        }

class ItemAddForm(forms.ModelForm):
    """Form definition for ItemAdd."""

    class Meta:
        model = Item
        # fields = '__all__'
        exclude = ['noteNumber']
        help_texts = {'quantity': "Nhập số lượng, ít nhất bằng 1",}
        widgets = {
        'deadline': DateInput(),
        }

class NoteUpdateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        widgets = {
            'noteNumber': forms.HiddenInput(),
            'receiveDay': DateInput()
        }

class ItemUpdateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'noteNumber': forms.HiddenInput(),
            'deadline': DateInput()
        }

class LogCreateForm(forms.ModelForm):
    """Form definition for LogCreate."""

    class Meta:
        """Meta definition for LogCreateform."""

        model = ItemLog
        fields = '__all__'
