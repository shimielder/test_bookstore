from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from bookstoreapp.models import Books, Authors
from bookstoreapp.forms import AuthorForm, BookForm
import logging

# Настройки логгера

logger = logging.getLogger(__name__)
loglevel = logging.INFO
logging.basicConfig(format='[%(asctime)s]  %(message)s', level=loglevel)


def main(request):
    return render(request, 'bookstoreapp\\main.html')


def show_books(request):
    logger.debug('Содержимое переменной "request" функции "show_books":\n{}'.format(request))
    context = dict()
    context['query'] = Books.objects.all().order_by('book_id')
    logger.debug('Содержимое переменной "context" функции "show_books":\n{}'.format(context))
    return render(request, 'bookstoreapp\\books.html', context)


def show_authors(request):
    logger.debug('Содержимое переменной "request" функции "show_authors":\n{}'.format(request))
    context = dict()
    context['query'] = Authors.objects.all().order_by('author_id')
    logger.debug('Содержимое переменной "context" функции "show_authors":\n'.format(context))
    return render(request, 'bookstoreapp\\authors.html', context)


def search(request):
    logger.debug('Содержимое переменной "request" функции "search":\n{}'.format(request))
    context = dict()
    if 'Search' in request.POST:
        search_data = Books.objects.all().filter(Q(book_title__icontains=request.POST['Search'])).order_by('book_id')
        if search_data:
            context['books_query'] = search_data
        search_data = Authors.objects.all().filter(Q(author_name__icontains=request.POST['Search'])).order_by(
            'author_id')
        if search_data:
            print(search_data)
            context['authors_query'] = search_data
    logger.debug('Содержимое переменной "context" функции "search":\n'.format(context))
    return render(request, 'bookstoreapp\\search.html', context)


def edit_author(request, author_id=None):
    logger.debug('Содержимое переменной "request" функции "edit_author":\n{}'.format(request))
    form = AuthorForm()
    try:
        existing_author = Authors.objects.get(author_id=author_id)
    except Authors.DoesNotExist:
        existing_author = None
    if request.method == 'POST':
        if existing_author:
            # Если автор существует, обновляем его данные в соответствии
            # с полученными из запроса данными
            logger.debug('Обновление книги:\n{}'.format(existing_author))
            form = AuthorForm(request.POST, instance=existing_author)
            if "Delete" in request.POST:
                logger.debug('Удаление книги:\n{}'.format(existing_author))
                existing_author.delete()
                return redirect(show_authors)
        else:
            form = AuthorForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'bookstoreapp\\edit_author.html', {'saved': True,
                                                                      'form': form})
    if existing_author:
        # Если при 'GET' запросе по author_id есть такой автор,
        # то подставляем данные автора в форму, иначе рендерим пустую форму
        # для добавления нового автора
        form = AuthorForm(instance=existing_author)
    return render(request, 'bookstoreapp\\edit_author.html', {'form': form})


def edit_book(request, book_id=None):
    logger.debug('Содержимое переменной "request" функции "edit_author":\n{}'.format(request))
    form = BookForm()
    try:
        existing_book = Books.objects.get(book_id=book_id)
    except Books.DoesNotExist:
        existing_book = None
    if request.method == 'POST':
        if existing_book:
            logger.debug('Обновление книги:\n{}'.format(existing_book))
            form = BookForm(request.POST, instance=existing_book)
            if "Delete" in request.POST:
                logger.debug('Удаление книги:\n{}'.format(existing_book))
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
