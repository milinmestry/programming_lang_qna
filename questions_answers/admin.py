from django.contrib import admin

from .models import Question, QuestionAnswer, QuestionChoice
from .forms import QuestionForm, QuestionAnswerForm

# Register your models here.

class QuestionChoiceInline(admin.TabularInline):
    fields = ['question_choice_text']
    model = QuestionChoice
    extra = 4

# class QuestionChoiceAdmin(admin.ModelAdmin):
#     fields = ['question_choice_text']

class QuestionAnswerInline(admin.StackedInline):
    form = QuestionAnswerForm
    fields = ['subjective_answer', 'answer_keywords']
    model = QuestionAnswer
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm
    fields = ['programming_language', 'question_type', 'question_text'
        , 'candidate_experienced', 'is_active']
    inlines = [QuestionChoiceInline, QuestionAnswerInline]


# admin.site.register(Question)
# admin.site.register(QuestionChoice)
admin.site.register(Question, QuestionAdmin)
