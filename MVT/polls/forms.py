from django.forms import ModelForm
from django.http import request
from django.utils import timezone, dateformat
from .models import Question, Choice
from django.contrib.auth.models import User

user = User


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = "__all__"
        # fields = ["question_text", "pub_date"]
        labels = {
            "question_text": "Topic",
        }

    help_texts = {
        "question_text": "Provide a topic for your Poll",
    }

    def __init__(self, *args, **kwargs):
        formatted_date = dateformat.format(timezone.now(), 'Y-m-d H:i:s')
        last_question = Question.objects.order_by("-pub_date")[0]
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['pub_date'].initial = formatted_date
        self.fields['user'].initial = user


class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'
        labels = {
            "choice_text1": "Choices",
            "choice_text2": "Choices",
            "choice_text3": "Choices",
            "choice_text4": "Choices",
        }

    help_texts = {
        "question_text": "Please provide at least two Choices for your Poll",
    }


def __init__(self, *args, **kwargs):
    last_question = Question.objects.last()
    super(QuestionForm, self).__init__(*args, **kwargs)
    self.fields['question_id'].initial = last_question.get(id())
    self.fields['votes'].initial = 0
