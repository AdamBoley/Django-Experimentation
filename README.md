To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.



Install Django:
`pip3 install 'django<4'`
Because we want the stable release version of Django, version 3, not the experimental v4


Access site-packages, which is where all of the packages, such as Django, are installed:
`cd /workspace/.pip-modules/lib/python3.8/site-packages/`

Then list all of the packages:
`ls -la`

Never change anything in this directory, since doing so can corrupt things

Go back to previous directory - the main directory:
`cd -`
or more explicitly:
`cd /workspace/Django-Experimentation`

Django has an admin command for starting projects:
`django-admin startproject django_todo .` for a project named django_todo. The dot . indicates that we want the project to be created in the current directory
This creates a directory / folder called django_todo and a separate manage.py file

The application can be run with:
`python3 manage.py runserver`
Without any pages or routes, a basic Django landing page will render, confirming that Django is installed and working properly

Create the first app, called todo:
`python3 manage.py startapp todo`
This creates another directory


If the terminal displays warnings about Unapplied Migrations:

`python3 manage.pt showmigrations` to see what migrations need to be made
Then:
`python3 manage.py migrate` to run the migrations
The `--plan` flag can be used here to see the steps that will be executed. This won't actually run the migrate command, it will just display what it will do

A superuser must be created in order to login and look at the database:
`python3 manage.py createsuperuser`
A name must be supplied, but an email is not necessary. A password must be supplied twice


Once a model has been created, or when models are changed:
`python3 manage.py makemigrations`
This creates a Python file in the migrations folder that holds the model template

The run the migrate command to create or update a database table

In this way, makemigrations and migrate act like git add., git commit -m, and git push

The dry-run flag can be applied to see what this command would do without actually doing it:
`python3 manage.py makemigrations --dry-run`





## Tests

Run tests in todo / tests.py:
`python3 manage.py test`

Run a specific test file:
`python3 manage.py test todo.<test-file-name>`
i.e.
`python3 manage.py test todo.test_forms`

### Coverage
Install the Coverage tool:
`pip3 install coverage`

Run Coverage:
`coverage run --source=todo manage.py test`
This creates a .coverage file in the repository

View the coverage report:
`coverage report`

Place coverage report into an interactive HTML file:
`coverage html`
Creates a folder called htmlcov that holds reports

Run non-Django web-server:
`python3 -m http.server`
This requires that a Django server not be running



## Deployment

Login to heroku:
`heroku login -i`
Supply password and email

Install psycopg2 to handle database deployment:
`pip3 install psycopg2-binary`

Install gunicorn:
`pip3 install gunicorn`
Gunicorn acts as a web server

Create requirements.txt file:
`pip3 freeze --local > requirements.txt`

Create heroku app using terminal:
`heroku apps:create adam-django-todo-app`

Check that the workspace has been linked to the Heroku app:
`git remote -v`

Create Heroku Postgres database (resources page)

Check that Heroku has added the postgres database:
`heroku addons`

Install dj_database_url:
`pip3 install dj_database_url`

Freeze requirements again

Get database url:
`heroku config`

In settings.py, import dj_database_url at top
Then replace the value of the default key in the DATABASES dictionary with the DATABASE_URL retrieved from `heroku config`

Migrate local SQLite3 database to remote Heroku Postgres database:
`python3 manage.py migrate`

add '*.sqlite3' to .gitignore, so that the database is not pushed to Github

The add, commit, push 

Push to Heroku:
`git push origin main`

This will likely fail, since this application contains no static CSS or JS files

Fix with:
`heroku config:set DISABLE_COLLECTSTATIC=1`

Push again, will likely fail with error code H14

Create Procfile, add:
`web: gunicorn django_todo.wsgi:application`
This tells Heroku that our app is a web app that requires a web-server, and hence allow it to handle HTTP requests

Push to Heroku (again)

This Django will throw an error about ALLOWED_HOSTS

Add URL of the deployed Heroku app to the ALLOWED_HOSTS array in settings.py, removing the prepended http:// and appended /

HOLY FUCKING SHIT IT WORKS

Clean up:

In settings.py, import os at the top of the file

Change the value of SECRET_KEY to:
os.environ.get('SECRET_KEY', [secret key here])

Change the value of ALLOWED_HOSTS to:
[os.environ.get('HEROKU_HOSTNAME')]

Change the value of DATABASES to:
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

Add these to CONFIG_VARS
HEROKU_HOSTNAME : deployed app URL








