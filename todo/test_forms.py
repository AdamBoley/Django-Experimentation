from django.test import TestCase
from .forms import ItemForm

# Create your tests here.
# this testing file will test the forms.py file
# the forms.py file controls the forms in the add_item and edit_item pages

class TestItemForm(TestCase):
    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})
        # instantiates a form, and gives an empty string as a name, simulating a user who has submitted a form without entering a name
        self.assertFalse(form.is_valid())
        # returns passed is it is false that the form is valid
        self.assertIn('name', form.errors.keys())
        # when a form is invalid, a dictionary is returned back, and this test checks to see if a key called 'name' is in that dictionary
        self.assertEqual(form.errors['name'][0], 'This field is required.')
        # checks to see if the first error message for the 'name' key is equal to 'This field is required.'
        # the form will return a list of errors, so we need to use the zero index
        # these three tests essentially test the same thing - that the name field is required and that an error will be raised if it is filled out

    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test'})
        # instantiates a form with a valid name input, but no done field
        # this should not matter, since the done checkbox has a default of false / unchecked in models.py
        self.assertTrue(form.is_valid())
        # asserts that it is true that the form is valid, which is should be with a valid name


    def test_fields_are_explicit_in_form_meta_class(self):
        # assumes that someone else has changed the Item model, but not updated everything else
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
        # ItemForm contains a sub-class called Meta, which contains fields, which is equal to ['name', 'done']
        # Should return as true if ItemForm remains unchanged
