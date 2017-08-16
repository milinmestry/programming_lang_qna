from django.contrib import admin

from .models import Question, QuestionChoice
from .forms import QuestionForm

# Register your models here.

class QuestionChoiceInline(admin.TabularInline):
    fields = ['question_choice_text']
    model = QuestionChoice
    extra = 4

# class QuestionChoiceAdmin(admin.ModelAdmin):
#     fields = ['question_choice_text']

class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm
    # fields = ['programming_language', 'question_type', 'question_text'
    #     , 'subjective_answer', 'answer_keywords'
    #     , 'candidate_experienced', 'is_active']
    fieldsets = (
        (None, {
            'fields' : ['programming_language', 'candidate_experienced'
                , 'question_type', 'question_text']
        }),
        ('Subjective Answer Details', {
            'fields' : ['subjective_answer', 'answer_keywords']
        }),
    )
    inlines = [QuestionChoiceInline]
    list_filter = ['question_type', ]


# admin.site.register(Question)
# admin.site.register(QuestionChoice)
admin.site.register(Question, QuestionAdmin)
