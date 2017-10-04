from django.shortcuts import render
from django.db.models import Count

from questions_answers.models import Question

# Create your views here.
def details(request, plid):
    question_list = Question.objects.filter(programming_language_id=plid) \
        .values('question_type') \
        .annotate(question_type_count = Count('question_type'))
    context = {'question_list': question_list}
    return render(request, 'questions_answers/details.html', context)
    # return render(request, 'polls/index.html', context)
    # return HttpResponse("Hello, world. You're at the questions_answers index.")
