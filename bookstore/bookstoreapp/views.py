from django.shortcuts import render, get_object_or_404, redirect
from bookstoreapp.models import Books, Authors
from bookstoreapp.forms import AuthorForm, BookForm


# Create your views here.
def main(request):
    context = {'show books': show_books,
               'show authors': show_authors}
    return render(request, 'bookstoreapp\\main.html', context)


def show_books(request):
    context = dict()
    context['query'] = Books.objects.all().order_by('book_id')
    return render(request, 'bookstoreapp\\books.html', context)


def show_authors(request):
    context = dict()
    context['query'] = Authors.objects.all().order_by('author_id')
    return render(request, 'bookstoreapp\\authors.html', context)


def search(request):
    context = dict()
    if 'Search' in request.POST:
        search_data = Books.objects.all().filter(book_title__search=request.POST['Search']).order_by('book_id')
        if search_data:
            context['books_query'] = search_data
        search_data = Authors.objects.all().filter(author_name__search=request.POST['Search']).order_by(
            'author_id')
        if search_data:
            print(search_data)
            context['authors_query'] = search_data
    return render(request, 'bookstoreapp\\search.html', context)


def edit_author(request, author_id=None):
    form = AuthorForm()
    try:
        existing_author = Authors.objects.get(author_id=author_id)
    except Authors.DoesNotExist:
        existing_author = None
    if request.method == 'POST':
        if existing_author:
            form = AuthorForm(request.POST, instance=existing_author)
            if "Delete" in request.POST:
                existing_author.delete()
                return redirect(show_authors)
        else:
            form = AuthorForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'bookstoreapp\\edit_author.html', {'saved': True,
                                                                      'form': form})
    if existing_author:
        form = AuthorForm(instance=existing_author)
    return render(request, 'bookstoreapp\\edit_author.html', {'form': form})


def edit_book(request, book_id=None):
    form = BookForm()
    try:
        existing_book = Books.objects.get(book_id=book_id)
    except Books.DoesNotExist:
        existing_book = None
    if request.method == 'POST':
        if existing_book:
            form = BookForm(request.POST, instance=existing_book)
            if "Delete" in request.POST:
                existing_book.delete()
                return redirect(show_books)
        else:
            form = BookForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'bookstoreapp\\edit_book.html', {'saved': True,
                                                                    'form': form})
    if existing_book:
        form = BookForm(instance=existing_book)
    return render(request, 'bookstoreapp\\edit_book.html', {'form': form})
