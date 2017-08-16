from django.db import models
from programming_languages.models import ProgrammingLanguage

# Create your models here.
class Question(models.Model):
    """
    Question alongwith its answer for the candidate.
    If question is objective, then the multiple choice options are stored
    in a separate table.
    """
    SUBJECTIVE = 'subjective'
    OBJECTIVE = 'objective'
    QUESTION_TYPE_CHOICES = (
        (SUBJECTIVE, 'Subjective'),
        (OBJECTIVE, 'Objective'),
    )

    question_type = models.CharField(max_length=20, choices=QUESTION_TYPE_CHOICES, default=SUBJECTIVE)
    question_text = models.TextField(max_length=1000)
    subjective_answer = models.TextField(max_length=4000, blank=True, null=True)
    answer_keywords = models.TextField(max_length=500, blank=True, null=True)
    candidate_experienced = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(blank=True, default=True)
    added_by = models.CharField(max_length=100, blank=True)
    added_on = models.DateTimeField(blank=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    deactivated_by = models.CharField(max_length=100, blank=True, null=True)
    deactivated_on = models.DateTimeField(blank=True, null=True)
    programming_language = models.ForeignKey(ProgrammingLanguage, on_delete=models.PROTECT)

    def __str__(self):
        return self.question_text

    class Meta:
        db_table = 'questions'


class QuestionChoice(models.Model):
    """
    When question is objective type then multiple choices are available to the end user.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    question_choice_text = models.CharField(max_length=500, null=True)
    is_active = models.BooleanField(default=True)
    added_by = models.CharField(max_length=100, blank=True)
    added_on = models.DateTimeField(blank=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    deactivated_by = models.CharField(max_length=100, blank=True, null=True)
    deactivated_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.question_choice_text

    class Meta:
        db_table = 'question_choices'
