from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Item
from django.shortcuts import get_object_or_404
from .forms import ItemForm


def home(request):
    return render(request, 'CRUD/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('items')  # Redirect to the items page after login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'CRUD/login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'There was an error with your registration.')
    else:
        form = UserCreationForm()
    return render(request, 'CRUD/register.html', {'form': form})

def items_view(request):
    items = Item.objects.all()  # Fetch all items from the database
    return render(request, 'CRUD/items.html', {'items': items})

def item_detail_view(request, pk):
    item = get_object_or_404(Item, pk=pk)  # Fetch the item by primary key (id)
    return render(request, 'CRUD/item_detail.html', {'item': item})

def add_item_view(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new item to the database
            return redirect('items')  # Redirect to the items page
    else:
        form = ItemForm()  # Display an empty form
    return render(request, 'CRUD/add_item.html', {'form': form})