from django.db import models

# Create your models here.

class Item(models.Model):  # inherits the model class, which is supplied by Django
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name



# name is a character field, so it can only contain text characters in it. max_length specifies the maximum number of characters
# null=False prevents the creation of records without an entry in the name field
# blank=False makes the name field required on all forms
# specifying these here means that the onus of checking is transferred to the database, not on whatever submits the information to create the record
# This is because tasks can be added using a web form or via the Django database
# done is a Boolean field, so it can only contain values of True or False
# default=False means that items are marked with False in the done column by default
# the __str__ function overrides the base model class string method that creates the name of the record in the table
# By default, this string method provides a generic, unhelpful name that makes it difficult to find records in the database
# Overriding the string method to produce a custom name as above makes it much easier to navigate the table
# These changes do not need to be committed in any way - saving and hard-refreshing does the trick 
