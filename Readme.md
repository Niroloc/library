# Установка и использования

## Установка
```bash
git clone https://github.com/Niroloc/library.git
cd linrary
docker-compose up --build -d
```
## Копирование тестовых данных в базу
```bash
psql postgresql://library:q61e6V5@0.0.0.0:6000/library < example_data.sql
```

# REST API

## GET

 - `GET http://0.0.0.0:8000/api/get/readers/` - Получение списка читателей с полями `id`, `name`, `events` в формате json
 - `GET http://0.0.0.0:8000/api/get/books/` - Получение списка книг с полями `id`, `author`, `name`, `available`, `taken`, `events` в формате json

Поля `events` в респонсах выше - списки событий взятия или возврата, связанные с данной книгой или читателем (взяли/вернули эту книгу, взял/вернул этот читатель)

## POST

 - `POST http://0.0.0.0:8000/api/post/readers/` - Загружка в базу списка новый читателей
Обязательное поле `name`. 
Пример запроса:
```bash
curl -X POST http://0.0.0.0:8000/api/post/readers/ -H 'Content-Type: application/json' -d '[{"name": "Иванов Иван Иванович"}]'
```
 - `POST http://0.0.0.0:8000/api/post/books/` - Загрузка в базу списка новых книг. Обязательные поля: `author`, `name`, `available`.
Пример запроса:
```bash
curl -X POST http://0.0.0.0:8000/api/post/books/ -H 'Content-Type: application/json' -d '[{"author": "А. С. Пушкин", "available": 5, "name": "Сказка о рыбаке и рыбке"}]'
 ```

 - `POST http://0.0.0.0:8000/api/post/event/` - Добавление события взятия или возврата книги в базу. При этом изменяется количество доступных для взятия книг. Обязательные поля `event_type`: [`taken`, `returned`], `book`: id взятой или возвращённой книги, `reader`: id взявшего или вернувшего книгу читателя.
Пример запроса:
```bash
curl -X POST http://0.0.0.0:8000/api/post/event/ -H 'Content-Type: application/json' -d '{"event_type": "taken", "book": 1, "reader": 1}'
 ```

 - `POST http://0.0.0.0:8000/api/post/load_file/` - Загрузка списка книг из файла `.csv`
Формат строки файла:
```csv
 [Имя автора книги], [Название книги], [Количество прихода]
 ```
Пример запроса:
```bash
curl -X POST -Ss http://0.0.0.0:8000/api/post/load_file/ -F "file=@/path/to/project/dir/testfile.csv"
```