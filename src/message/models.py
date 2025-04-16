from django.db import models

class Message(models.Model):
    """
    Model representing a message.
    """
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey('chat.Chat', on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='messages')

    def __str__(self):
        return f"Message {self.id} in {self.chat.title}"