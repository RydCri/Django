import datetime
from django.utils import timezone
from django.db import models
from django.forms import ModelForm


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return f"{self.question_text} {self.pub_date}"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text1 = models.CharField(max_length=200, null=False)
    choice_text2 = models.CharField(max_length=200, null=True)
    choice_text3 = models.CharField(max_length=200, null=True)
    choice_text4 = models.CharField(max_length=200, null=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.question} {self.votes}"
