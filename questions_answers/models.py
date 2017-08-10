from django.db import models
from programming_languages.models import ProgrammingLanguage

# Create your models here.
class Question(models.Model):
    """

    """
    SUBJECTIVE = 'subjective'
    OBJECTIVE = 'objective'
    QUESTION_TYPE_CHOICES = (
        (SUBJECTIVE, 'Subjective'),
        (OBJECTIVE, 'Objective'),
    )

    programming_language = models.ForeignKey(ProgrammingLanguage, on_delete=models.PROTECT)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPE_CHOICES, default=SUBJECTIVE)
    question_text = models.CharField(max_length=750)
    candidate_experienced = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(blank=True)
    added_by = models.CharField(max_length=100, blank=True)
    added_on = models.DateTimeField(blank=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    deactivated_by = models.CharField(max_length=100, blank=True, null=True)
    deactivated_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.question_text

    class Meta:
        db_table = 'questions'


class QuestionChoice(models.Model):
    """
    When question is objective type then multiple choices are available to the end user.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    question_choice_text = models.CharField(max_length=200)
    is_active = models.BooleanField(blank=True)
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


class QuestionAnswer(models.Model):
    """
    Answer for the question.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    question_choice = models.ForeignKey(QuestionChoice, on_delete=models.CASCADE)
    subjective_answer = models.CharField(max_length=3000)
    answer_keywords = models.CharField(max_length=300)
    is_active = models.BooleanField(blank=True)
    added_by = models.CharField(max_length=100, blank=True)
    added_on = models.DateTimeField(blank=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    deactivated_by = models.CharField(max_length=100, blank=True, null=True)
    deactivated_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.subjective_answer

    class Meta:
        db_table = 'question_answers'
