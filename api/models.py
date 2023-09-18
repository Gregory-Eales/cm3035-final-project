from django.db import models


# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=256, db_index=True)
    image = models.FileField(blank=False)
    user_id = models.IntegerField(blank=False, db_index=True)
    def __str__(self):
        return self.name


# add model for post

class Post(models.Model):
    '''
    model for storing text posts of the user
    '''

    user_id = models.IntegerField(blank=False, db_index=True)
    content = models.CharField(max_length=256, db_index=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)


class Friend(models.Model):

    '''
    model for storing friends
    '''
    
    friender_id = models.IntegerField(blank=False, db_index=True)
    friendee_id = models.IntegerField(blank=False, db_index=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)


