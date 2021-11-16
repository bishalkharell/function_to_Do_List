from django.urls import path,include
from .views import todoList,update,search,delete,create

urlpatterns = [
    path('',todoList),
    path('create/',create,name='create'),
    path('update/<int:id>',update,name='update'),
    path('delete/<int:id>',delete,name='delete'),
    path('search',search)
]
