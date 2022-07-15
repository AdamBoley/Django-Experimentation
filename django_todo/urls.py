"""django_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo.views import get_todo_list, add_item, edit_item, toggle_item, delete_item
# an alternative way to import these function from views.py would be 'import views', and then prepend views. to each function call - i.e. views.add_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_todo_list, name='get_todo_list'),
    path('add', add_item, name='add'),
    path('edit/<item_id>', edit_item, name='edit'),
    path('toggle/<item_id>', toggle_item, name='toggle'),
    path('delete/<item_id>', delete_item, name='delete')
]

# the hello path calls the say_hello function in todo/views.py
# when running the server, /hello must be appended to the url in the url bar
# this will render a simple html page with the text 'hello'
# the third entry, add, corresponds to the href of the anchor tag in todo_list.html
# in the fourth entry, the angular bracket takes in the item's id and this is the way by which an id make its way from a link or form, through the URL and into the view
# in views.py, item_id is a paramter in the edit_item function
