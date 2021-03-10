from django.forms import ModelForm
from .models import ToDoList

class ListForm(ModelForm):
    class Meta:
        model = ToDoList
        fields = ['textField']
        labels = {'textField':'Enter Here'}
