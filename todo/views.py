from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from .forms import (
    Todo, TodoForm
)

# ------------------------------------
# Function Based Views
# ------------------------------------

# List:
def todo_list(request):
    return render(request, 'list.html', {
        "todos": Todo.objects.all()
    })

# Add:
def todo_add(request):
    form = TodoForm(request.POST or None)

    if form.is_valid():
        form.save()
        # Message:
        messages.success(request, 'Kaydedildi.')
        # If OK redirect:
        return redirect('todo_list') # redirect('path_name')

    context = {
        "form": form
    }
    return render(request, 'add.html', context)


def todo_update(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)
    if request.method== "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Güncellendi.')
            return redirect("index")
    return render(request, 'update.html', {
        'form': form,
        'todo': todo
    })


def todo_delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    messages.success(request, 'Silindi.')
    return redirect("index")