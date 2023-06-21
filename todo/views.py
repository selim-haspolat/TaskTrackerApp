from django.shortcuts import render
from .forms import (
    Todo, TodoForm
)

def todo_list(request):
    todos = Todo.objects.all()  
    context = {
        'todos': todos
    }
    return render(request, 'list.html', context)