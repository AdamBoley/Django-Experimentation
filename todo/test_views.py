from django.test import TestCase
from .models import Item

# Create your tests here.

class TestViews(TestCase):
    

    def test_get_todo_list(self):
        response = self.client.get('/')
        # grabs the home page
        self.assertEqual(response.status_code, 200)
        # confirms that the home page has loaded correctly, since status_code 200 indicates a good response
        self.assertTemplateUsed(response, 'todo/todo_list.html')
        # confirms that the correct template was rendered


    def test_get_add_item_page(self):
        response = self.client.get('/add')
        # grabs the add_item page, uses add because that is what is in the urlpatterns array
        self.assertEqual(response.status_code, 200)
        # confirms that the home page has loaded correctly, since status_code 200 indicates a good response
        self.assertTemplateUsed(response, 'todo/add_item.html')
        # confirms that the correct template was rendered


    def test_get_edit_item_page(self):
        item = Item.objects.create(name='Test')
        # creates a table entry
        response = self.client.get(f'/edit/{item.id}')
        # grabs the edit_item page, uses edit because that is what is in the urlpatterns array, and item.id is the id of the entry created in the table as part of the test
        self.assertEqual(response.status_code, 200)
        # confirms that the home page has loaded correctly, since status_code 200 indicates a good response
        self.assertTemplateUsed(response, 'todo/edit_item.html')
        # confirms that the correct template was rendered


    def test_can_add_item(self):
        response = self.client.post('/add', {'name': 'Test'})
        # posts a form with a name of Test
        self.assertRedirects(response, '/')
        # confirms that after a form is submitted, the app redirects the user back to the home page, /


    def test_can_delete_item(self):
        item = Item.objects.create(name='Test')
        # creates a table entry
        response = self.client.get(f'/delete/{item.id}')
        # deletes the entry from the table
        self.assertRedirects(response, '/')
        # confirms that after a form is submitted, the app redirects the user back to the home page, /
        existing_items = Item.objects.filter(id=item.id)
        # tries to get the deleted item from the table
        self.assertEqual(len(existing_items), 0)
        # since the item should have been deleted, the existing_items variable should just be an empty list, and hence have a length of 0


    
    def test_can_toggle_item(self):
        item = Item.objects.create(name='Test', done=True)
        # creates a table entry
        response = self.client.get(f'/toggle/{item.id}')
        # toggles the item's done status
        self.assertRedirects(response, '/')
        # confirms that after the item's done status has changed, the app redirects the user back to the home page, /
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)
        # after the toggle, updated_item.done should be False
        self.assertEqual(updated_item.done, False)
        # this would also work, and is a bit more explicit, since it checks whether updated_item.done is False


    def test_can_edit_item(self):
        item = Item.objects.create(name='Test')
        # creates a table entry
        response = self.client.post(f'/edit/{item.id}', {'name': 'new test'})
        # tests the update item functionality, and changes the entry's name from 'Test' to 'new test'
        self.assertRedirects(response, '/')
        # confirms that after the item's done status has changed, the app redirects the user back to the home page, /
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'new test')
