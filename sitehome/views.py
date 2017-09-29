from django.shortcuts import render
# from django.shortcuts import get_object_or_404, render

from programming_languages.models import ProgrammingLanguage

# Create your views here.
def home(request):
    active_proglang = ProgrammingLanguage.objects.filter(is_active = 1)
    # .values('question_type').annotate(question_type_count = Count('question_type'))
    context = {'proglangList': active_proglang}
    return render(request, 'sitehome/home.html', context)
