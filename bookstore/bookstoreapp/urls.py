"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from bookstoreapp.views import main, show_books, show_authors, edit_author, edit_book, search


urlpatterns = [
    url(r'^$', main, name='main page'),
    url(r'^books/$', show_books, name='show books'),
    url(r'^authors/$', show_authors, name='show authors'),
    url(r'^authors/add/$', edit_author, name='add author'),
    url(r'^books/add/$', edit_book, name='add book'),
    url(r'^books/(?P<book_id>[0-9]+)/edit/$', edit_book, name='edit book'),
    url(r'^authors/(?P<author_id>[0-9]+)/edit/$', edit_author, name='edit author'),
    url(r'^search$', search, name='search'),
]
