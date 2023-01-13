from django.db import models

# Create your models here.

class Message(models.Model):
    user = models.CharField("老師名字", max_length = 20)
    subject = models.CharField("專業", max_length = 10)
    content = models.TextField("評論")
    publication_date = models.DateTimeField("Time",auto_now_add=True)

    def __str__(self):
        return self.subject
    
