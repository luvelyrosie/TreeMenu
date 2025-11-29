# Django Tree Menu App

A full-featured Django application for displaying a tree-structured menu using a template tag. The menu is stored in the database, editable through the standard Django admin, and determines the active item based on the current URL. The project fully meets the requirements of the test assignment.

## Implemented Requirements

1. Menu is rendered via template tag: `{% draw_menu 'main_menu' %}`
2. All items above the active one are expanded
3. First-level children under the active item are expanded
4. All data is stored in the database
5. Editable via Django Admin
6. Multiple menus can exist on a page (identified by name)
7. Supports both direct URLs and named URLs
8. Rendering the menu executes exactly **one** DB query
9. Uses only Django and Python standard library

---

# Running the Project

Two options are supported:

* **Docker (recommended)** — fast and convenient
* Local run — if needed

---

# Running via Docker (recommended)

## 1. Install Docker

[https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

## 2. Clone the repository

```
git clone https://github.com/luvelyrosie/TreeMenu.git
cd TreeMenu
```

## 3. Run

```
docker-compose up --build
```

Docker will automatically:

* create containers
* apply migrations
* create a superuser:

**Login:** admin
**Password:** admin
**Email:** [admin@example.com](mailto:admin@example.com)

---

# Accessing the Application

Application:
[http://localhost:8000/](http://localhost:8000/)

Admin:
[http://localhost:8000/admin/](http://localhost:8000/admin/)

---

# Creating Menu Items

To display the menu on the main page, create a menu item in the admin with the field:

`Menu = main_menu`

### MenuItem Fields Description:

#### **Menu**

Menu name (e.g., **main_menu** to display on the main page).

#### **Title**

Displayed text of the item.

#### **Parent**

Optional. Allows nesting.

#### **URL**

Direct URL (e.g., `/`). Leave empty if using named URL.

#### **Named URL**

Django route name (e.g., `home`).

#### **Named URL kwargs**

Parameters, example:

```
{"id": 5}
```

#### **Order**

Sorting order (lower = higher).

#### **Open in new tab**

Open link in a new tab.

#### **Image**

Optional image. Defaults used if not specified.

---

# Usage in Templates

```
{% load draw_menu %}
{% draw_menu 'main_menu' %}
```

---

# Local Run (without Docker)

## 1. Clone

```
git clone https://github.com/luvelyrosie/TreeMenu.git
cd TreeMenu
```

## 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate       # Windows
cd TreeMenu
```

## 3. Install dependencies

```
pip install -r requirements.txt
```

## 4. Run PostgreSQL manually

## 5. Migrations

```
python manage.py migrate
```

## 6. Create superuser

```
python manage.py createsuperuser
```

## 7. Run server

```
python manage.py runserver
```

---

# Features

* Fully dynamic tree menu
* Stored in DB
* Auto-highlight active item
* 1 SQL query per menu
* Supports named URL and kwargs
* Convenient admin interface
* Production-ready in Docker





# Django Tree Menu App

Полнофункциональное Django‑приложение для отображения древовидного меню с использованием template tag. Меню хранится в базе данных, редактируется через стандартную админку Django и определяет активный пункт по текущему URL. Проект полностью соответствует требованиям тестового задания.

## Реализованные требования

1. Меню выводится через template tag: `{% draw_menu 'main_menu' %}`
2. Все элементы над активным раскрыты
3. Первый уровень вложенности под активным пунктом раскрыт
4. Всё хранится в базе данных
5. Редактирование через Django Admin
6. На странице может быть несколько меню (определяются по имени)
7. Поддержка прямых URL и named URL
8. На отрисовку меню выполняется ровно **один** запрос к БД
9. Используется только Django и стандартная библиотека Python

---

# Запуск проекта

Поддерживаются два варианта:

- **Docker (рекомендуется)** — быстро и удобно
- Локальный запуск — при необходимости

---

# Запуск через Docker (рекомендуется)

## 1. Установите Docker  
https://docs.docker.com/get-docker/

## 2. Клонируйте репозиторий
```
git clone https://github.com/luvelyrosie/TreeMenu.git
cd TreeMenu
```

## 3. Запуск
```
docker-compose up --build
```

Docker автоматически:

- создаст контейнеры
- применит миграции
- создаст суперпользователя:

**Логин:** admin  
**Пароль:** admin  
**Email:** admin@example.com  

---

# Доступ к приложению

Приложение:  
http://localhost:8000/

Админка:  
http://localhost:8000/admin/

---

# Создание пунктов меню

Чтобы меню появилось на главной странице, создайте в админке пункт меню с полем:

`Menu = main_menu`

### Описание полей MenuItem:

#### **Menu**
Имя меню (например **main_menu**, чтобы меню отображалось на главной странице).

#### **Title**
Отображаемый текст пункта.

#### **Parent**
Необязательно. Позволяет вложенность.

#### **URL**
Прямой URL (например, `/`).  
Оставьте пустым, если используете named URL.

#### **Named URL**
Имя маршрута Django (например, `home`).

#### **Named url kwargs**
Параметры, пример:
```
{"id": 5}
```

#### **Order**
Порядок сортировки (меньше — выше).

#### **Open in new tab**
Открывать ссылку в новой вкладке.

#### **Image**
Опциональное изображение. Если не указано — используется дефолт.

---

# Использование в шаблонах

```
{% load draw_menu %}
{% draw_menu 'main_menu' %}
```

---

# Локальный запуск (без Docker)

## 1. Клонирование
```
git clone https://github.com/luvelyrosie/TreeMenu.git
cd TreeMenu
```

## 2. Создание виртуального окружения
```
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate       # Windows
cd TreeMenu
```

## 3. Установка зависимостей
```
pip install -r requirements.txt
```

## 4. Запустите PostgreSQL вручную

## 5. Миграции
```
python manage.py migrate
```

## 6. Создание суперпользователя
```
python manage.py createsuperuser
```

## 7. Запуск сервера
```
python manage.py runserver
```

---

# Особенности

- Полностью динамическое древовидное меню
- Хранение в БД
- Авто‑подсветка активного элемента
- 1 SQL‑запрос на меню
- Поддержка named URL и kwargs
- Удобная админка
- Готово к продакшену в Docker