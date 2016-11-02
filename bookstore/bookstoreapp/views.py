from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from bookstoreapp.models import Books, Authors
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def main(request):
    context = {'show books': show_books,
               'show authors': show_authors}
    return render(request, 'bookstoreapp\\main.html', context)

def show_books(request):
    context = dict()
    context['query'] = Books.objects.all()
    return render(request, 'bookstoreapp\\books.html', context)


def show_authors(request):
    context = dict()
    context['query'] = Authors.objects.all()
    return render(request, 'bookstoreapp\\authors.html', context)


def edit_author(request, author_id):
    if "cancel" in request.POST:
        return redirect('main_page')
    context = dict()
    try:
        author = Authors.objects.get(author_id=author_id)
    except ObjectDoesNotExist:
        return render(request, 'bookstoreapp\\edit_author.html', context)
    context['author id'] = author_id
    context['author name'] = author.author_name
    return render(request, 'bookstoreapp\\edit_author.html', context)


def save_author(request):
    context = {}
    try:
        author = Authors(author_name=request.POST['author_name'])
        author.save()
    except Exception as e:
        context['error_message'] = e
    else:
        context['succsessful'] = True
    return render(request, 'bookstoreapp\\edit_author.html', context)


def edit_book(request, book_id):
    if "cancel" in request.POST:
        return redirect('main_page')
    context = dict()
    book = Books.objects.filter(book_id=book_id)
    pass
