from django.shortcuts import render
from django.db.models import Count
# from django.shortcuts import get_object_or_404, render

from programming_languages.models import ProgrammingLanguage
from questions_answers.models import Question

# Create your views here.

# SELECT a.*, b.`question_type`, b.`qtCount`
# FROM
# (
# 	select `programming_language_id`, `question_type`, count(`question_type`) AS qtCount
#     from questions where 1 group by `programming_language_id`,`question_type`
# ) AS b
# RIGHT JOIN prog_lang_qna.`programming_languages` AS a
# ON a.`id`=b.`programming_language_id`
# ORDER BY a.`programming_lang`;

def home(request):
    active_proglang = ProgrammingLanguage.objects.filter(is_active = 1) \
        .annotate(question_type_count = Count('question__question_type')) \
    # .values('question__question_type') \

    # active_proglang = Question.objects.filter(programming_language__is_active = 1) \
    #     .annotate(question_type_count = Count('programming_language__programming_lang'))
        # .values('programming_language__programming_lang', 'question_type') \

    # print(active_proglang)
    # context = {'proglangList': []}
    context = {'proglangList': active_proglang}
    return render(request, 'sitehome/home.html', context)
