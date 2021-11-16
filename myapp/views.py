from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from .forms import ListForm
from .models import ToDoList
import json
from django.core import serializers
# Create your views here.


def todoList(request):
    obj = ToDoList.objects.all()
    form = ListForm
    context = {
        'obj': obj,
        'form' : form

    }
    return render(request,'index.html',context)

def create(request):
    if request.method =='POST':
        form = ListForm(request.POST)
        form.save()
        return redirect('/')
    
    
def update(request,id):
    person = ToDoList.objects.get(id=id)
    if request.method =='POST':
        data = request.POST['textField']
        person.textField = data
        person.save()
        return redirect('/')
    content={
        'person':person
    }  
    return render(request,'update.html',content)


def delete(request,id):
    person = ToDoList.objects.get(id=id or None)
    person.delete()
    return redirect('/')

def search(request):
    query = request.GET['query']
    allPost = ToDoList.objects.filter(textField__icontains=query)
    posting = {'allPost':allPost}

    return render(request,'search.html',posting)


