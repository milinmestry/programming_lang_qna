from django import forms

class QuestionForm(forms.ModelForm):
    question_text = forms.CharField(widget=forms.Textarea)


class QuestionAnswerForm(forms.ModelForm):
    subjective_answer = forms.CharField(widget=forms.Textarea)