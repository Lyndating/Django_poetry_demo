https://rasulkireev.com/managing-django-with-poetry/

## Managing a Django project with poetry

1. install poetry
      `pip3 install --user poetry` 
2. creat a directory fir Django project
      `mkdir django_poetry_demo && cd django_poetry_demo`
3. Initiate a poetry project
      `poetry init`
4. Add dependencies
      `poetry add django`
5. Start Django project
      `poetry run django-admin startproject django_poetry_demo .`
6. Working on Django Project
7. check version of Django installed
      `poetry run python -m django --version`
8. development server
      `cd mysite`
      `poetry run python manage.py runserver`
9.  create app in the same directory
      `poetry run python manage.py startapp polls`
      
10. database setup
      `poetry run python manage.py migrate`
      to create all necessary database tables based on `INSTALLED_APPS` under the `settings.py` file
11. check database tables
      `sqlite3 db.sqlite3`
      `SELECT * FROM table_name`
      `.schema table_name`
1.   


