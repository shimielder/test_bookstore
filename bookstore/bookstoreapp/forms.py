from django import forms
from bookstoreapp.models import Books, Authors


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = ('author_name',)


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ('book_title', 'author', 'pages_count')
