from django.shortcuts import render, redirect
from items.models import Category, Item
from django.contrib import messages
from django.contrib.auth import logout
from . import views
from .forms import SignupForm

# Create your views here.
def index(request):
    # this condition will filter the 8 items only!
    # items = Item.objects.filter(sold_out=False)[0:8]
    items = Item.objects.all()
    categories = Category.objects.all()
    
    return render(request, 'core/index.html',{
        'categories': categories,
        'items':items,
    })
def contact(request):
    return render (request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html', {
        'form': form
    })
    
def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged Out!"))
    return redirect('core:index')