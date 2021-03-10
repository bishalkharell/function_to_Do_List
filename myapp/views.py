from django.shortcuts import render,redirect
from .forms import ListForm
from .models import ToDoList
# Create your views here.

def todoList(request):
    # newForm = ListForm()
    # if request.method == 'POST':
    #     data = request.POST
    #     field = data['textField']
    #     obj = ToDoList.objects.create(textField=field)
    #     return redirect('/')
    # else:
    #     person = ToDoList.objects.all()

    #     content = {
    #         'person':person,
    #         'name':newForm
    #     }
    newForm = ListForm()
    if request.method =='POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    person = ToDoList.objects.all()
    content = {
        # 'person':person,
        'name':newForm,
        'person':person
    }
    return render(request,'index.html',content)


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
    person = ToDoList.objects.get(id=id or none)
    person.delete()
    return redirect('/')

def search(request):
    query = request.GET['query']
    allPost = ToDoList.objects.filter(textField__icontains=query)
    posting = {'allPost':allPost}

    return render(request,'search.html',posting)


