from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    """
    Model representing a chat.
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats')

    def __str__(self):
        return self.title