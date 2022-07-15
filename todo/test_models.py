from django.test import TestCase
from .models import Item

# Create your tests here.
# models.py does not require extensive testing
# this is because it is a small file and most of it is imported / inherited from Django anyway
# the stuff from Django has already been extensively tested, we assume

class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='test')
        # creates a table entry, with a name of test and an unspecified done status
        self.assertFalse(item.done)
        # Confirms that the created item's done status is false
        self.assertEqual(item.done, False)
        # this would also work, and is a bit more explicit


    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='test')
        # creates a table entry, with a name of test and an unspecified done status
        self.assertEqual(str(item), 'test')
        # confirms that the string method in models.py returns a string of the name, in this case 'test'
