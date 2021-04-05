from django.urls import path

from mainapp.views import RemindersView, RemindersCreateView, RemindersUpdateView, RemindersDeleteView

app_name = 'mainapp'

urlpatterns = [
    path('', RemindersView.as_view(), name='index'),
    path('create/', RemindersCreateView.as_view(), name='create-reminder'),
    path('update/<int:pk>', RemindersUpdateView.as_view(), name='update-reminder'),
    path('delete/<int:pk>', RemindersDeleteView.as_view(), name='delete-reminder')
]