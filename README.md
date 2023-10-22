# Quiz_test

## Установка и настройка

### Требования
- Python 3.8+
- Docker
- Docker Compose

### Шаги установки

#### 1. Настройка базы данных
- Создайте в корне проекта файл .env и заполните его данными для подключения к базе данных, используя шаблон dotenv.example.

#### 2. Соберите и запустите докер-образ:
В корне проекта, где находится файл docker-compose.yml, запустите докер-образы:
``` docker compose up -d```

#### 3. Подключитесь к созданному контейнеру и выполните миграции БД:
```docker exec backend python manage.py migrate```

#### 4. Соберите статику бэкенда для админки (НЕОБЯЗАТЕЛЬНО):
``` docker compose exec backend python manage.py collectstatic ```
``` docker exec backend cp -r /app/collected_static/. /backend_static/static/ ```

#### 5. Готово! Веб-сервис доступен по адресу http://localhost:8000/api/


## Пример запроса:
```curl -X POST -H "Content-Type: application/json" -d '{"questions_num": 2}' http://localhost:8000/api/questions/get_question/```

Ответ API: 
```
{
    "question_id": 177602,
    "question_text": "In \"Winnie-the-Pooh\", Piglet tries to capture one of these imaginary elephant-like creatures",
    "answer_text": "a Heffalump",
    "created_at": "2023-10-22T15:23:57.058865Z"
},
{
    "question_id": 57741,
    "question_text": "In 1799 he overthrew the Directory & became first consul",
    "answer_text": "Napoleon",
    "created_at": "2023-10-22T15:23:57.065899Z"
}
]
```