from django.db import models
from django.utils import timezone

# Create your models here.

class Word(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    inum = models.IntegerField(default=0)
    due_date = models.DateTimeField(timezone.now())
    active = models.BooleanField(default=False)
    chapter = models.IntegerField(default=0)


    def __str__(self):
        return "{} {} {} {} {} {}".format(self.question, self.answer, self.inum, self.due_date, self.active, self.chapter)
    
