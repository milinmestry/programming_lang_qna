from django.contrib import admin
from django.utils import timezone
from django.forms.models import BaseInlineFormSet


from .models import Question, QuestionChoice
from .forms import QuestionForm

from django.http import HttpResponse #temp

# Register your models here.

class QuestionChoiceInline(admin.TabularInline):
    fields = ['question_choice_text', 'choice_answer']
    model = QuestionChoice
    extra = 4

class QuestionChoiceInlineFormset(BaseInlineFormSet):
    def save_new(self, form, commit=True):
        return super(QuestionChoiceInlineFormset, self).save_new(form, commit=commit)

    def save_existing(self, form, instance, commit=True):
        return form.save(commit=commit)

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
        print(obj)

        obj.added_by = request.user
        obj.added_on = timezone.now()
        super().save_model(request, obj, form, change)

    # def save_formset(self, request, form, formset, change):
    #     return HttpResponse(form)
    #
    #     instances = formset.save(commit=False)
    #     for instance in instances:
    #         instance.added_by = request.user
    #         instance.added_on = timezone.now()
    #
    #         instance.questionChoice.added_by = request.user
    #         instance.questionChoice.added_on = timezone.now()
    #         instance.save()
    #     formset.save_m2m()

    class Media:
        js = ("questions_answers/js/admin/first.js", )


# admin.site.register(Question)
# admin.site.register(QuestionChoice)
admin.site.register(Question, QuestionAdmin)
