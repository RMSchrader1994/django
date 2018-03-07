from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import TodoItem
from .forms import TodoItemForm, EditTodoItemForm

def edit_todo_item(request, id):
    item = get_object_or_404(TodoItem, pk=id)
    form = EditTodoItemForm(instance=item)
    if request.method == "POST":
        print("POST")
        form = EditTodoItemForm(request.POST, instance=item)
        if form.is_valid():
         form.save()
         return redirect("/")
    else:
        print("GET")
    return render(request, "todo/todo_item_form.html", {'form': form})

def get_todo_page(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        print("Get")
    
    form = TodoItemForm()
    items = TodoItem.objects.all()
    return render(request, "todo/todo_items.html", {'items':items, 'form':form})
    
def delete_todo_item(request, id):
    item = get_object_or_404(TodoItem, pk=id)
    item.delete()
    return redirect("/")
    
def toggle_todo_item(request, id):
    item = get_object_or_404(TodoItem, pk=id)
    item.gone = not item.gone
    
    item.save()
    return redirect("/")