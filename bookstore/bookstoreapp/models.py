from django.db import models


class Authors(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_name = models.CharField(unique=True, max_length=200)

    def __str__(self):
        return (self.author_name)

    class Meta:
        managed = False
        db_table = 'authors'


class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_title = models.CharField(unique=True, max_length=200)
    author = models.ForeignKey(Authors, models.DO_NOTHING)
    pages_count = models.SmallIntegerField()

    def __str__(self):
        return (self.book_title)

    class Meta:
        managed = False
        db_table = 'books'
