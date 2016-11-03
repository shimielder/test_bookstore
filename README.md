Web-приложение по управлению книжной библиотекой

1. Данные хранятся в СУБД PostgreSQL

2. Редактирование доступно любому пользователю запустившему приложение

3. Приложение позволяет управлять списком книг (добавить / удалить / редактировать книгу):
    - ID
    - Название
    - Автор
    - Количество страниц

  Приложение позволяет управлять списком авторов (добавить / удалить / редактировать автора):
    - ID
    - Имя

4. Связь между книгами и авторами — многие ко многим.

5. Поиск книг по названию либо автору.

Использованные технологии:

Python 3.5
PostgreSQL 9.6
Django 1.10.2
psycopg2 2.6.2
