from django.db import models

class File(models.Model):
    """
    Model representing a file.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    content_type = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.name