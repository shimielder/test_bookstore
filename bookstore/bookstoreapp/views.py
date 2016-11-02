from django.shortcuts import render
from django.http import HttpResponse
from bookstoreapp.models import Books, Authors


# Create your views here.

def show_books(request):
    return render(request, Books.objects.all())


def show_authors(request):
    return render(request, Authors.objects.all())
