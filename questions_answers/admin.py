from django.contrib import admin
from django.utils import timezone


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
                , 'question_text', 'question_type']
        }),
        ('Subjective Answer Details', {
            'classes': ('subjective-answer',),
            'fields' : ['subjective_answer', 'answer_keywords']
        }),
    )
    inlines = [QuestionChoiceInline]

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        obj.added_on = timezone.now()
        super().save_model(request, obj, form, change)

    class Media:
        js = ("questions_answers/js/admin/first.js", )


# admin.site.register(Question)
# admin.site.register(QuestionChoice)
admin.site.register(Question, QuestionAdmin)
