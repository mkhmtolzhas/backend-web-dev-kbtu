from django.db import models

class Message(models.Model):
    class AuthorType(models.TextChoices):
        USER = 'user', 'User'
        LLM = 'llm', 'LLM'

    id = models.AutoField(primary_key=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author_type = models.CharField(
        max_length=10,
        choices=AuthorType.choices,
        default=AuthorType.USER
    )
    chat = models.ForeignKey('chat.Chat', on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='messages', null=True, blank=True)
    file = models.ForeignKey('s3.File', on_delete=models.SET_NULL, null=True, blank=True, related_name='messages')

    def __str__(self):
        return f"Message {self.id} in {self.chat.title} by {self.author_type}"
