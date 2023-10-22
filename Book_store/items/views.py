from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .form import NewItemForm
from .models import Item, Category


def browser(request):
    category_id = request.GET.get('category', 0)
    query = request.GET.get('query', '')
    categories = Category.objects.all()
    items = Item.objects.filter(sold_out=False)
    
    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains= query) | Q(descripion__icontains=query))    
    
    return render(request, 'items/browser.html', {
        'items': items,
        'query': query,
        'categories': categories,
        "category_id": int(category_id)
        
        
    })
# Create your views here.

def detail(request, pk):
    items = get_object_or_404(Item, pk=pk)
    releted_items = Item.objects.filter(category =items.category, sold_out=False).exclude(pk=pk) [0:3]
    
    
    return render(request, 'items/detail.html', {
        'items': items,
        'releted_items':releted_items
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            
            return redirect('items:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'items/form.html', {
        'form': form,
        'title': 'New item',
        })    
 