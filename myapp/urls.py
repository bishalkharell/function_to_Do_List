from django.urls import path,include
from .views import todoList,update,search,delete

urlpatterns = [
    path('',todoList),
    path('update/<int:id>',update,name='update'),
    path('delete/<int:id>',delete,name='delete'),
    path('search',search)
]
