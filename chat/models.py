from django.db import models

class Message(models.Model):

    '''
    model for storing chat messages
    '''

    sender_id = models.IntegerField(blank=False, db_index=True)
    receiver_id = models.IntegerField(blank=False, db_index=True)
    content = models.CharField(max_length=256, db_index=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)