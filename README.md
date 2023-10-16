# inclusive-care-prototype

## Запуск проекта
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
### 4. Запуск сервера
```
python manage.py runserver
```
