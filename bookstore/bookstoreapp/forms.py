from django import forms
from bookstoreapp.models import Books, Authors


class AuthorForm(forms.ModelForm):
    author_name = forms.CharField(max_length=200, help_text="Введите имя автора")

    class Meta:
        model = Authors
        fields = ('author_name',)


class BookForm(forms.ModelForm):
    book_title = forms.CharField(max_length=200, help_text="Введите название книги")
    author = forms.CharField(max_length=200)
    pages_count = forms.IntegerField()

    class Meta:
        model = Books
        fields = ('book_title', 'author', 'pages_count')
