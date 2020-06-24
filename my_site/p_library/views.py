from django.http import HttpResponse
from django.template import loader
from p_library.models import Book, Author, Publishing
from django.shortcuts import render, redirect

# Create your views here.


def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)


def index(request):
    template = loader.get_template('index.html')

    books = Book.objects.all()
    books_list = [i for i in books]
    biblio_data = {'title': 'My library',
                   'books': books_list}

    return HttpResponse(template.render(biblio_data, request))


def show_publishings(request):
    """Показывает издательства и их книги по пути /publish
    Я решил, что вывести просто список издательств будет скучно,
    потому вывел таблицу в которой перечислены издательства, 
    а книги сгруппированы по издательствам(см /publish)."""

    template = loader.get_template('publishings/publishings.html')
    books = Book.objects.all()
    pubs = Publishing.objects.all()
    books_list = [i for i in books]
    pubs_list = [i for i in pubs]
    b_data = {'books': books_list, 'pubs': pubs_list}
    return HttpResponse(template.render(b_data, request))


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if book.copy_count < 1:
                return redirect('/index/')
            else:
                book.copy_count -= 1
        book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')
