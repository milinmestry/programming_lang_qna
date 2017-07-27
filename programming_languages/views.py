from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect #
from django.urls import reverse

# from .models import Choice, Question

# Create your views here.

def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # return render(request, 'polls/index.html', context)
    return HttpResponse("Hello, world. You're at the polls index.")
