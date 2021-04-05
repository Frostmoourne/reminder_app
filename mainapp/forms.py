from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm
from django import forms
from .models import ReminderModel


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class ReminderForm(BSModalModelForm):
    class Meta:
        model = ReminderModel
        # fields = '__all__'
        exclude = ['is_active', 'description']
        widgets = {
            'reminder_time': DateTimeInput()
        }
