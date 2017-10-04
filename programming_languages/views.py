from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect #
from django.urls import reverse
from django.views import generic
from django.db.models import Count


from .models import ProgrammingLanguage
from questions_answers.models import Question

# Create your views here.

def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # return render(request, 'polls/index.html', context)
    return HttpResponse("Hello, world. You're at the polls index.")


class DetailView(generic.DetailView):

    model = ProgrammingLanguage
    template_name = 'programming_languages/details.html'

    def get_queryset(self):
        # print('pk=', self.request.GET)
        """
        Exclude any questions thar aren't published yet.
        """
        return Question.objects.filter(pk=1) \
            .annotate(question_type_count = Count('question_type'))
