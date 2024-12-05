from django.db import models

# Create your models here.
from django.db import models

class Chat(models.Model):
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message