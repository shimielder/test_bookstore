from django.shortcuts import render, redirect
from django.http import HttpResponse
from bookstoreapp.models import Books, Authors


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
