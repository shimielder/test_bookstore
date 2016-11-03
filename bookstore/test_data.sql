CREATE TABLE IF NOT EXISTS authors (
              author_id serial PRIMARY KEY,
              author_name varchar (200) UNIQUE NOT NULL
              );
              
CREATE TABLE IF NOT EXISTS books (
              book_id serial PRIMARY KEY,
              book_title varchar (200) UNIQUE NOT NULL,
              author_id serial REFERENCES authors,
              pages_count smallint NOT NULL
              );
              
INSERT INTO authors (author_name) VALUES 
              ('����� ������'),
              ('������� �����'),
              ('��������� ������'),
              ('����� �������'),
              ('������ ������'),
              ('��� �������'),
              ('���� �������'),
              ('������ �������'),
              ('������ ������');
              

INSERT INTO books (book_title, author_id, pages_count) VALUES 
              ('� ������ ����� ���', (SELECT author_id FROM authors WHERE author_name = '����� ������'), 451),
              ('����� �����', (SELECT author_id FROM authors WHERE author_name = '������� �����'), 516),
              ('����� ������ � ����������� ������', (SELECT author_id FROM authors WHERE author_name = '����� �������'), 324),
              ('����� ������ � ������ �������', (SELECT author_id FROM authors WHERE author_name = '����� �������'), 414),
              ('����� ������ � ����� ��������', (SELECT author_id FROM authors WHERE author_name = '����� �������'), 612),
              ('������� ������', (SELECT author_id FROM authors WHERE author_name = '��������� ������'), 201),
              ('������� ������', (SELECT author_id FROM authors WHERE author_name = '������ ������'), 105),
              ('����� � ���. ��� 1', (SELECT author_id FROM authors WHERE author_name = '��� �������'), 900),
              ('����� � ���. ��� 2', (SELECT author_id FROM authors WHERE author_name = '��� �������'), 831),
              ('����� � ���. ��� 3', (SELECT author_id FROM authors WHERE author_name = '��� �������'), 934),
              ('���� �� ����', (SELECT author_id FROM authors WHERE author_name = '���� �������'), 551),
              ('���� � ������', (SELECT author_id FROM authors WHERE author_name = '���� �������'), 478),
              ('���� � ����', (SELECT author_id FROM authors WHERE author_name = '���� �������'), 598),
              ('��� ��� �����', (SELECT author_id FROM authors WHERE author_name = '������ �������'), 350),
              ('�������� ��������', (SELECT author_id FROM authors WHERE author_name = '������ �������'), 414),
              ('��� ������� ���������', (SELECT author_id FROM authors WHERE author_name = '������ �������'), 463),
              ('���� ���������', (SELECT author_id FROM authors WHERE author_name = '������ ������'), 857),
              ('����� �������', (SELECT author_id FROM authors WHERE author_name = '������ ������'), 919),
              ('���� �����', (SELECT author_id FROM authors WHERE author_name = '������ ������'), 1024),
              ('��� ������������', (SELECT author_id FROM authors WHERE author_name = '������ ������'), 895);