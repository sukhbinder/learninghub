from django.db import models
from django.utils import timezone

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{} {}".format(self.id, self.name)


class Word(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    inum = models.IntegerField(default=0)
    due_date = models.DateTimeField(default=timezone.now())
    active = models.BooleanField(default=False)
    chapter = models.IntegerField(default=0)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    isvoiceonly = models.BooleanField(default=False)

    def __str__(self):
        return "{} {} {} {} {} {} {}".format(self.subject, self.question, self.answer, self.inum, self.due_date, self.active, self.chapter)
    
