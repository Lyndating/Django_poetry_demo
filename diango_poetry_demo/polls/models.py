from secrets import choice
from django.db import models
# import models module from django.db

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # if question is deleted, delete all the related choices
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)