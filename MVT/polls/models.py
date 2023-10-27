import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    user = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING, null=True)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return f"{self.question_text} {self.pub_date} {self.user}"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, null=False)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.question} {self.votes}"
