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









