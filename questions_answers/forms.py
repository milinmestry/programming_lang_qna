from django.forms import ModelForm, Textarea
from questions_answers.models import Question

class QuestionForm(ModelForm):
    # question_text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Question
        
        fields = ('programming_language', 'question_type', 'question_text'
            , 'subjective_answer', 'answer_keywords'
            , 'candidate_experienced', 'is_active')
        # widgets = {
        #     'question_text': Textarea(attrs={'cols': 80, 'rows': 10}),
        # }
