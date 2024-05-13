Початковий запуск Django-додатку:
Створення віртуального середовища:

Встановлення Python та пакету virtualenv, якщо вони ще не встановлені.

Створення віртуального середовища для ізоляції залежностей Django-додатку.

Клонування репозиторію та перехід до проекту:
Клонування репозиторію Django-проекту з GitHub

Перехід до каталогу проекту у терміналі або командному рядку.

Встановлення залежностей Django-проекту:

Активація віртуального середовища.

Встановлення всіх залежностей, зазначених у файлі requirements.txt.

Застартовування сервера Django:

Запуск сервера Django для перевірки коректності налаштувань та функціоналу.

Виконання команди python manage.py runserver.

Перевірка доступності веб-інтерфейсу:
Відкриття браузера та переход на локальний URL, щоб переконатися, що веб-інтерфейс працює коректно.

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

py .\manage.py runserver

Головне для кодингу локально :
DEBUG = True
ALLOWED_HOSTS = []

DEBUG = True
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['final-project-goit-web-antonbabenko.koyeb.app']
ALLOWED_HOSTS = []

git fetch origin main : Отримає останні зміни з гілки main вашого віддаленого репозиторію.
git reset --hard origin/main : Встановить вашу локальну гілку main на ту ж точку, що і гілка main вашого віддаленого репозиторію, і видалить будь-які локальні зміни, які ви не зберегли.
