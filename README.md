# Тестовое задание для SibDev

## Шаг 1: Клонировать репозиторий
```
git clone git@github.com:dsahfjkahsdfklashdfl/test_sibdev.git
```
## Шаг 2: Добавить значения в .env файл

Пример значений находится в файле .env
(Да там секрет лежит нормальный, думаю все при деплое свой ставят новый. Поэтому это не ошибка, что я его не убрал.)

## Шаг 3: Запуск приложения при помощи Docker
```
sudo docker compose up
```
Создастся суперюзер с логином admin и паролем admin

## Шаг 4: Зайти в админку

Находится по http://0.0.0.0:8000/admin/

Данные для входа указаны на Шаге 3

![image](https://github.com/dsahfjkahsdfklashdfl/test_sibdev/assets/137927196/e0c6bff0-26a8-4e12-98d2-2bddff74096a)

## Шаг 5: Проверка эндпоинтов
Фронт реализовал в виде сваггера)))  http://0.0.0.0:8000/api/swagger/

### Эндпоинт для добавления данных (тестовый файл лежит в репозитории) 

![image](https://github.com/dsahfjkahsdfklashdfl/test_sibdev/assets/137927196/d1170d4f-b4fe-4bcb-b569-fd7273e7e8fa)


Пример ответа 


![image](https://github.com/dsahfjkahsdfklashdfl/test_sibdev/assets/137927196/0dfb4be2-2c5d-4bb9-a2a2-80a005f342f5)


Данные сохраняются в базу, можно посмотреть в админке


![image](https://github.com/dsahfjkahsdfklashdfl/test_sibdev/assets/137927196/c01f3774-0865-4cb1-91c7-8b57b763d72c)

### Эндпоинт выдачи обработанных данных 


![image](https://github.com/dsahfjkahsdfklashdfl/test_sibdev/assets/137927196/6fccb4f8-5d8a-4105-8c57-eff38a2beaf5)


Пример ответа 

![image](https://github.com/dsahfjkahsdfklashdfl/test_sibdev/assets/137927196/83be5c6e-78c6-4b32-9747-4d3acc30ab29)


