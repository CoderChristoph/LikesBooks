from __future__ import unicode_literals
from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __repr__(self):
        return "< User Object: FName: {}, LName: {}, Email: {} >".format(self.first_name, self.last_name, self.email)

class Book(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.CharField(max_length = 255)
    uploaded_books = models.ForeignKey(User, related_name="uploader")
    user_liked_books = models.ManyToManyField(User, related_name="liked_users")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __repr__(self):
        return "< User Object: Name: {}, Desc: {}, Uploaded Books: {}, User Liked Books: {} >".format(self.name, self.desc, self.uploaded_books.first_name, self.user_liked_books)