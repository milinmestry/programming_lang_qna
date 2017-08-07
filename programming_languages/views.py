from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect #
from django.urls import reverse
from django.views import generic


from .models import ProgrammingLanguage

# Create your views here.

def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # return render(request, 'polls/index.html', context)
    return HttpResponse("Hello, world. You're at the polls index.")


class DetailView(generic.DetailView):
    model = ProgrammingLanguage
    template_name = 'programming_languages/details.html'

    # def get_queryset(self):
    #     """
    #     Exclude any questions thar aren't published yet.
    #     """
    #     return Question.objects.filter(pub_date__lte=timezone.now())
