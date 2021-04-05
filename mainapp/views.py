from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView

from .forms import ReminderForm
from .models import ReminderModel


class RemindersView(ListView):
    model = ReminderModel
    context_object_name = 'reminders'
    template_name = 'mainapp/remindermodel_list.html'


class RemindersCreateView(BSModalCreateView):
    template_name = 'mainapp/remindermodel_form.html'
    form_class = ReminderForm
    success_message = 'Success: Reminder was created.'
    success_url = reverse_lazy('mainapp:index')


class RemindersUpdateView(BSModalUpdateView):
    template_name = 'mainapp/remindermodel_update.html'
    form_class = ReminderForm
    success_message = 'Success: Reminder was updated.'
    success_url = reverse_lazy('mainapp:index')


class RemindersDeleteView(BSModalDeleteView):
    template_name = 'mainapp/remindermodel_delete.html'
    form_class = ReminderForm
    success_message = 'Success: Reminder was updated.'
    success_url = reverse_lazy('mainapp:index')
