from django.shortcuts import render, redirect, get_object_or_404
from .models import Book


def index(request):
    books = Book.objects.all()
    return render(request, 'crud/index.html', {'books': books})


def add(request):
    if request.method == "POST":
        if request.POST['title'] and request.POST['author'] and request.POST['price']:
            new_book = Book(
                title=request.POST['title'], author=request.POST['author'], price=request.POST['price'])
            new_book.save()
            return redirect('index')
        else:
            return redirect('add')
    return render(request, 'crud/add.html')


def edit(request, book_id):
    book = Book.objects.get(pk=book_id)

    if request.method == "POST":
        if request.POST['title'] and request.POST['author'] and request.POST['price']:
            book.title = request.POST['title']
            book.price = request.POST['price']
            book.author = request.POST['author']
            book.save()
            return redirect('index')

    return render(request, 'crud/edit.html', {'book': book})


def delete(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()

    return redirect('index')
