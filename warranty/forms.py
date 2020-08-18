from django import forms
from .models import Note, Item

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
        labels = {
            'itemName': "Tên sản phẩm",
            'quantity': 'Số lượng',
            'itemGroup': 'Nhóm sản phẩm',
            'status': 'Tình trạng tiếp nhận',
            'check': 'Kiểm tra',
            'conclude': 'Đánh giá',
            'deadline': 'Deadline',
            'note': 'Ghi chú',
            'done': "Xong/ Chưa xong"
        }
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