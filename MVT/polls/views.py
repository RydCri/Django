from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import Http404
from django.utils import timezone

from .forms import QuestionForm, ChoiceForm
from .models import Choice
from .models import Question


def polls(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "polls.html", context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        creator = User.objects.get(pk=question.user_id).username
        context = {
            'question': question,
            'creator': creator
        }
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "poll_detail.html", context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls_results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    user = request.user
    if user.is_authenticated:
        try:
            selected_choice = question.choice_set.get(pk=request.POST["choice"])
            selected_choice.votes += 1
            selected_choice.save()
        except (KeyError, Choice.DoesNotExist):
            return render(
                request,
                "poll_results.html",
                {
                    "question": question,
                    "error_message": "You didn't select a choice.",
                },
            )
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse("results", args=(question.id,)))


def new_poll(request):
    user = request.user
    if request.method == 'POST' and user.is_authenticated:
        formset = QuestionForm(request.POST)
        if formset.is_valid():
            formset.save(commit=False)
            formset.save()
            return HttpResponseRedirect('/polls/createChoice')
    else:
        form = QuestionForm()
        return render(request, "create_poll.html", {"form": form})


def new_choice(request):
    if request.method == 'POST':
        formset = ChoiceForm(request.POST)
        if formset.is_valid():
            formset.save(commit=False)
            formset.save()
            return HttpResponseRedirect('/polls/')
    else:
        form = ChoiceForm()
        return render(request, "create_choice.html", {"form": form})
