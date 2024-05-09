##  Варіант_1 перейти за посиланням

- <a href="https://final-project-goit-web-antonbabenko.koyeb.app/"><img src="static/img/newsletter.png" alt="Назва зображення" width="40" height="40"></a>  [Site "Fox.Web.Assistant"](https://final-project-goit-web-antonbabenko.koyeb.app/)  

##  Варіант_2 для завантаження тестового варіанту rel_2.0.
- docker pull antonbabenko1983/finalprojectgoitweb:web
- docker run -d -p 8000:8000 --name my_web_app antonbabenko1983/finalprojectgoitweb:web

##  Варіант_3 для завантаження тестового варіанту  the latest version
- [Архів](https://github.com/IT-School-GoIT/FinalProjectGoitWeb/archive/refs/heads/main.zip)
- або
- [Clone](https://github.com/IT-School-GoIT/FinalProjectGoitWeb.git) 
- docker-compose up

## Вхід но наповненної бази
- Username:  admin123
- Password:  admin123


# Технічне завдання на створення застосунку “Personal Assistant” (Web application)

## Основний функціонал Web application виконаний на Django
### Завдання:
Студентам пропонується виконати апдейт “персонального помічника”, реалізованого по завершенню курсу Python Core,  для чого необхідно створити web-інтерфейс та розширити можливості основного додатка.

### Основні вимоги до проекту “Personal Assistant”:
1. Зберігати контакти з іменами, адресами, номерами телефонів, email та днями народження до книги контактів;
2. Виводити список контактів, у яких день народження через задану кількість днів від поточної дати;
3. Перевіряти правильність введеного номера телефону та email під час створення або редагування запису та повідомляти користувача у разі некоректного введення;
4. Здійснювати пошук контактів серед контактів книги;
5. Редагувати та видаляти записи з книги контактів;
6. Зберігати нотатки з текстовою інформацією;
7. Проводити пошук за нотатками;
8. Редагувати та видаляти нотатки;
9. Додавати в нотатки "теги", ключові слова, що описують тему та предмет запису;
10. Здійснювати пошук та сортування нотаток за ключовими словами (тегами).
11. Виконувати завантаження файлів користувача на хмарний сервіс та мати доступ до них. Користувач повинен мати можливість через web-інтерфейс завантажити на сервер будь-який файл та завантажити його.
12. Сортувати файли користувача за категоріями (зображення, документи, відео та ін.) і відображати тільки обрану категорію (фільтр файлів за категорією).
13. Надавати коротке зведення новин за день. Для цього ви повинні вибрати будь-яку цікаву вам область (фінанси, спорт, політика, погода) та кілька інформаційних ресурсів на задану тематику. З вибраних ресурсів збирати на запит користувача інформацію (заголовки новин, курси валют, результати спортивних подій тощо) і відображати на сторінці результатів. Що саме збирати та як можете визначити самостійно.

### Вимоги до Аутентифікації
1. Реалізуйте механізм авторизації користувача для “Personal Assistant”. Web-інтерфейс повинен давати доступ до своїх функцій лише зареєстрованим користувачам. 
2. Кожен зареєстрований користувач повинен мати доступ лише до своїх даних та файлів. 
3. Реалізуйте механізми відновлення пароля для користувача за email

### Критерії прийому:
1. Web-інтерфейс може бути реалізований на фреймворку Django.
2. Проєкт має бути збережений в окремому репозиторії та бути загальнодоступним (GitHub, GitLab або BitBucket).
3. Проєкт містить докладну інструкцію щодо встановлення та використання.
4. “Personal Assistant” зберігає інформацію в базі даних і може бути перезапущений без втрати даних.
5. Для надійності та підвищення продуктивності всю інформацію зберігати у базі даних PostgreSQL.
6. Всі критичні дані до доступу до бази даних та налаштування програми зберігаються в змінних середовищах і не завантажуються в репозитарій.
7. Проєкт повністю реалізує всі пункти вимог, описані в завданні.



### Release plan
0. Release 0.1 - Start
1. Release 1.0 - implement features from 1 to 10
2. Release 1.1 - implement feature 11
3. Release 1.2 - implement feature 12
4. Release 1.3 - implement feature 13
3. Release 2.0 - implement user iteraction interface (replace terminal commands iteraction)

# Branch naming
Use feature / release flow style Example: 
branch name to work on feature feature/FoxWeb-Ticket## 
branch name for releale releale/release-1.0 major branch always main

1. Keep main always in working condition (No errors,failures allowed) , merge into main releale branches only after PR approves from team members , merged branch should be green .
2. Never!!!!! rename main branch
3. To start work on new feature ticket , create new branch from upcoming release branch . When work on feature done , create Pull Request into release branch , add reviewers into your PR. After work on PR comments and final approves from team merge feature branch into release branch.
4. Do not temper to add comments into your code . Team members will appreciate your work.
