# inclusive-care-prototype

## Используемые порты

```
8000 - Django
```

## Необходимые виртуальные переменные

### Пример

В данной папке записывается в файле .env

```
DEBUG=True
SECRET_KEY=django-insecure
```

### DEBUG

В целях разработки ставится значение `True`

### SECRET_KEY

Может быть сгенерирован на https://djecrety.ir/. В файле .env без кавычек

## Запуск проекта через python

### 1. Создание виртуального окружения (Опционально)

```
python -m venv venv
# Активация на системах UNIX
source venv/bin/activate
# Активация на системах Windows (bash)
source venv/Scripts/activate
```

### 2. Установка пакетов

```
pip install -r requirements.txt
```

### 3. Запуск миграций

```
python manage.py migrate
```

### 4. Создание администратора

```
python manage.py createsuperuser
```

### 5. Запуск сервера

```
python manage.py runserver
```

## Запуск проекта через docker-compose

```
sudo docker compose up --build -d
sudo docker exec -it inclusive-care-prototype-django-1 python manage.py migrate
sudo docker exec -it inclusive-care-prototype-django-1 python manage.py createsuperuser
```
