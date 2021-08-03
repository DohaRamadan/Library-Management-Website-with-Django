from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import BookForm, CategoryForm
# Create your views here.

# the index page 
def index(request):    
    if request.method == 'POST':        
        add_book = BookForm(request.POST, request.FILES)        
        if add_book.is_valid():
            add_book.save()
            return redirect('/')


        add_category= CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()
            return redirect('/')

    context = {
        'category' : Category.objects.all(),
        'books' : Book.objects.all(),
        'form' : BookForm(),
        'CatForm' : CategoryForm(), 
        'allbooks' : Book.objects.filter(active=True).count(),
        'soldbooks' : Book.objects.filter(status='sold').count(),
        'rentedbooks' : Book.objects.filter(status='rented').count(),
        'availablebooks' : Book.objects.filter(status='available').count(),

    }
    return render(request, 'pages/index.html', context)


# the books page
def books(request):
    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)


    context = {
        'category' : Category.objects.all(),
        'books' : search,
        'CatForm' : CategoryForm(),
    }
    return render(request, 'pages/books.html',context)


# the update page
def update(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST' :
        book_save = BookForm(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else: 
        book_save = BookForm(instance=book_id)
    context = {
          'form' : book_save,
          'CatForm' : CategoryForm(),
          'category' : Category.objects.all(),
          'books' : Book.objects.all(),
          'soldbooks' : Book.objects.filter(status='sold').count(),
          'rentedbooks' : Book.objects.filter(status='rented').count(),
          'availablebooks' : Book.objects.filter(status='available').count(),
    }
    return render(request,'pages/update.html', context)


# the delete page 
def delete(request, id):
    book_delete = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    return render(request, 'pages/delete.html')
