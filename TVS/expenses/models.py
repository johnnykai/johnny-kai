from django.db import models

class Expense(models.Model):
    
    CATE_CHOICES = (
      (0, "0"),
      (1, "1"),
      (2, "2"),
      (3, "3"),
      (4, "4"),
      (5, "5"),
    )

    target = models.IntegerField('Target', default=0)
    score = models.IntegerField('分數', default=0, choices=CATE_CHOICES)

    def __str__(self):
        return self.score

# Create your models here.
