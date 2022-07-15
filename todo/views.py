from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)
# The standard way to render an HTML document
# the items variable holds all of the entries in the Items table of the database
# These items can be displayed by adding them to the context dictionary and passing context to the return render statement


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
        # name = request.POST.get('item_name')
        # done = 'done' in request.POST
        # Item.objects.create(name=name, done=done)
        # the commented out lines refer to a previous build which processed a form we created ourselves
        # since we are now using a standard pre-built Django form, we need to use the above syntax
        # the is_valid method checks to see if the submitted form is valid per the blank and null statements in the models.py file
            

    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)

# the if statement in add_item handles users submitting the form. The name and done variables grab the values from the form object using the input name attributes
# An actual entry in the database is created using the Item.object.create method
# name=name and done=done are a bit confusing, but this because the variable names match the variables in the Item model and hence the column headers in the database
# This is both the benefit and curse of using harmonised syntax
# the return redirect command redirects the user to the todo items page, so that they can view their updated items


def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)

# get_object_or_404 is a Django shortcut and is used when we want to get an instance of the Item model
# form = ItemForm(instance=item) is used as in add_item, but instance=item pre-populates the form


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')


# item.done = not item.done flips the done status from whatever it currently is, i.e. false to true
# this function then saves and redirects back to the list of items
# whilst it may not seem like it, the page does actually do things and does refresh, but it is very quick


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')

