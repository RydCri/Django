from attr.filters import exclude
from django.forms import ModelForm
from .models import Question, Choice


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        exclude = ['pub_date']
        labels = {
            "question_text": "Topic",
        }
    help_texts = {
        "question_text": "Provide a topic for your Poll",
    }


class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        exclude = ["votes", "question"]
        labels = {
            "choice_text1": "Choices",
            "choice_text2": "Choices",
            "choice_text3": "Choices",
            "choice_text4": "Choices",
        }
    help_texts = {
        "question_text": "Please provide at least two Choices for your Poll",
    }
