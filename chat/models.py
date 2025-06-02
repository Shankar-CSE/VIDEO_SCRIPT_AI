# # from django.db import models

# # Create your models here.
# from django.db import models
# import datetime

# class history(models.Model):
#     input = models.CharField(max_length=100)
#     response = models.TextField(max_length=100)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return f"Input: {self.input}, Response: {self.response}, Timestamp: {self.timestamp}"


# chat/models.py

from django.db import models

class ChatHistory(models.Model):
    input = models.CharField(max_length=255)
    response = models.JSONField()  # Use TextField if Django version is old
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.input} - {self.date_time.strftime('%Y-%m-%d %H:%M:%S')}"
