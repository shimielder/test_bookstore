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
              ('Олдос Хаксли'),
              ('Герберт Уэллс'),
              ('Александр Пушкин'),
              ('Джоан Роулинг'),
              ('Сергей Есенин'),
              ('Лев Толстой'),
              ('Юрий Никитин'),
              ('Андрей Белянин'),
              ('Джордж Мартин');
              

INSERT INTO books (book_title, author_id, pages_count) VALUES 
              ('О дивный новый мир', (SELECT author_id FROM authors WHERE author_name = 'Олдос Хаксли'), 451),
              ('Война миров', (SELECT author_id FROM authors WHERE author_name = 'Герберт Уэллс'), 516),
              ('Гарри Поттер и Философский камень', (SELECT author_id FROM authors WHERE author_name = 'Джоан Роулинг'), 324),
              ('Гарри Поттер и Тайная комната', (SELECT author_id FROM authors WHERE author_name = 'Джоан Роулинг'), 414),
              ('Гарри Поттер и узник Азкабана', (SELECT author_id FROM authors WHERE author_name = 'Джоан Роулинг'), 612),
              ('Евгений Онегин', (SELECT author_id FROM authors WHERE author_name = 'Александр Пушкин'), 201),
              ('Сборник стихов', (SELECT author_id FROM authors WHERE author_name = 'Сергей Есенин'), 105),
              ('Война и Мир. Том 1', (SELECT author_id FROM authors WHERE author_name = 'Лев Толстой'), 900),
              ('Война и Мир. Том 2', (SELECT author_id FROM authors WHERE author_name = 'Лев Толстой'), 831),
              ('Война и Мир. Том 3', (SELECT author_id FROM authors WHERE author_name = 'Лев Толстой'), 934),
              ('Трое из леса', (SELECT author_id FROM authors WHERE author_name = 'Юрий Никитин'), 551),
              ('Трое в песках', (SELECT author_id FROM authors WHERE author_name = 'Юрий Никитин'), 478),
              ('Трое и боги', (SELECT author_id FROM authors WHERE author_name = 'Юрий Никитин'), 598),
              ('Меч без имени', (SELECT author_id FROM authors WHERE author_name = 'Андрей Белянин'), 350),
              ('Свирепый ландграф', (SELECT author_id FROM authors WHERE author_name = 'Андрей Белянин'), 414),
              ('Век святого Скиминока', (SELECT author_id FROM authors WHERE author_name = 'Андрей Белянин'), 463),
              ('Игра Престолов', (SELECT author_id FROM authors WHERE author_name = 'Джордж Мартин'), 857),
              ('Битва королей', (SELECT author_id FROM authors WHERE author_name = 'Джордж Мартин'), 919),
              ('Буря мечей', (SELECT author_id FROM authors WHERE author_name = 'Джордж Мартин'), 1024),
              ('Пир стервятников', (SELECT author_id FROM authors WHERE author_name = 'Джордж Мартин'), 895);