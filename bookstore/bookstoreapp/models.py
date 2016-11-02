from __future__ import unicode_literals

from django.db import models


class Authors(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_name = models.CharField(unique=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'authors'


class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_title = models.CharField(unique=True, max_length=200)
    author = models.ForeignKey(Authors, models.DO_NOTHING)
    pages_count = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'books'
