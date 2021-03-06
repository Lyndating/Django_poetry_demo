
## Managing a Django project with poetry ([django-demo-docs](https://www.djangoproject.com/start/))

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
      * to check the model classes : `from polls.models import class_names`
      * to create new
      `q = Class_Name(class_field1="string", class_field2=timezone.now())`
      `q.save()` to save into the database.

      * to text custom method
      `q1 = Question.objects.gt(pk=1)`
      `q1.was_published_recently()` => true
      * check choices from related object set
      `q1.choice_set.all()`
      * create choices 
      `q1.choice_set.create(choice_text="Not much", votes =0)`
      `q1.choice_set.create(choice_text="The sky", votes =0)`
      `q1.choice_set.create(choice_text="Just hacking again", votes=0)`

      * check vice versa
      `q1.choice_set.all()` return query set
      `q1.choice_set.count()` return number

      * delete choices
      `c = q1.choice_set.filter(question__pub_date__year=current_year)`
      `c.delete()`

17. check Database
      `Question.objects.all()`
      `Question.objects.filter(id=1)`
      `Question.objects.filter(question_text__startswith='What')`
      * filter return a query set, one or more.
      `[QuerySet <>,<>,<>]`
      

      * get return a single object. `<>`
      `Question.ojects.get(pub_date__year=current_year)`
      if there are more or none exist, it will raise an exception (Error msg)

18. create an admin user
      `poetry run python manage.py createsuperuser`
      `poetry run python manage.py runserver` and under `http:/127.0.0.1:8000/admin/` should see the admins'login page.
19. add views and url paths
    * in views.py:
      `def function_name(request, argument):`
      `return HttpResponse("response msg")`
    * in urls.py:
      `urlpatterns =[... path("/<type:argument>/", views.function_name, name="function_name"),]`
20.  use template to render html file
      `loader.get_template(html_file)`
      `context = {"variable_name": python_objects}`
      `return HttpResponse(template.render(context, request))`
21.  render() as a shortcut
22.  `from django.shortcuts import render`
      `return render(request, "polls/index.html", context)`
23.  raise 404 error
      `from django.http import Http404`
      use `try...except..else` block to raise error.
      then return render content and pass question object
      `return render(request, "polls/details.html", {"question": question})`.
24.  shortcuts - get_object_or_404
      `from django.shortcuts import get_object_or_404`
      use the shortcuts to call get() function and take Query.set and other arguments and raise Http404 if the object doesn't exist.
      `question = get_object_or_404(Question, pk=question_id)`.
      * there is another `get_list_or_404()` function, which using `filter()`instead of `get()` and raise 404 if the list is empty.
25.  add app_name in urls.py to specify individual url path.
      `app_name = 'polls'` before assign the `urlpatterns` array.
26.  removing hardcoded URLS by using template tag `{% url%}`
      `<a hrf="{% url "polls:detail" question_id %}">`
27.  Request and response objects
      * when page is requested, Django create an `HttpRequest` object that contains metadata about the the request. Then Djnago load the appropriate view, passing the `HttpRequest`as the first argument to the view function. 
28.  csrf_token
      * the server generates these tokens, links them to the user session and stores them in the database. 
      * They are then injected into any form presented to the client as a hidden field.
29.  Use Generic Views 
      There are two generic views: `ListView` and `DetailView`.
      * `DetailView` is executing `self.object` containg the object that view is operating upon.
      * `ListView` is executing `self.object_list` containing the list of objects (usually, but not neccssarily a queryset) that view is operating upon. 
      * amend URLconf in urls.py
        `path('<int:pk>/results', views.ResultsView.as_view(), name="results'),`

      * amend views in views.py
        `from django.views import generic`
        `class ResultsView(generic.DetailView)`
        `model = Question`
        `template_name = 'polls/results.html'`
30.  Automated Testing
      * identify problems
      * testing work done for you by the system
      * you could check your code still working as originally intended even making changes.
      * prevent the errors or problems 
      * TDD: write testing before coding. 

31.  Running tests in application 
      * in `polls/tests.py` create a test to expose bugs
      * running tests: `poetry run python manage.py test polls`
      * `manage.py est polls` will find a subclass of `django.test.TestCase`and look for test methods - whose names begin with `test`
      * create a Question instance and use `assertIS()` method to test
32.  Running Django test client
      * run test in the `shell` - setup the test env first: `poetry run python manage.py shell`
        * `from django.test.utils import setup_test_environment`
        * `setup_test_environment` - install template renderer to examine additional attributes on responses.
        * `from django.test import Client` - create an instance: `client= Client()`
33.  Running tests for ListView
      * also using `Client` to create an instance and using `reverse` to generate Url from View Name, e.g.: `polls:index`.
      * in `tests.py` to create a shorcut function to create new question for test.
      * to create new question and take two arguments: `Question.objects.create(question_text=question_text, pub_date= time)`
      * to create new test class: 
        * create new question: `create_question(question_text="test q", days=num_input)`
        * get response `self.client.get(reverse('polls:index'))`
        * test: `self.assertQuerysetEqual(response.context['latest_question_list'], [question])`, or if no_question_test, it should return [] empty array, or if multiply questions_test, it should return an array of questions in reverse order.
34.  Running tests for DetaillView


