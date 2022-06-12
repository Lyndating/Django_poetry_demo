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
12. create models
13. Activating models and make migration
      `poetry run python manage.py makemigrations polls`
      add polls config to `INSTALLED_APPS` in `settings.py`
      create database tables
14. take mirgration name to return SQL: 
      `poetry run python manage.py sqlmigrate polls 0001`
      it doesn't actually run the migration on db. 
      could also do: 
      `poetry run python manage.py check`
15. create model tables in database:
      `poetry run python manage.py migrate`
16. python shell to play with APIs
      `poetry run python manage.py shell`
      to check the model classes : `from polls.models import class_names`
      to create new
      `q = Class_Name(class_field1="string", class_field2=timezone.now())`
      `q.save()` to save into the database.
17. a


