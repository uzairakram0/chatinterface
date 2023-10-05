from django.db import models

# Create your models here.
class ChatMessage(models.Model):
    SENDER_CHOICES = [
        ('User', 'User'),
        ('Agent', 'Agent'),
    ]
    sender = models.CharField(max_length=10, choices=SENDER_CHOICES)
    content = models.TextField()

    def __str__(self):
        return f"{self.sender}: {self.content}"

class ApiKey(models.Model):
    key = models.CharField(max_length=500) # You can adjust the max length according to your needs.
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key