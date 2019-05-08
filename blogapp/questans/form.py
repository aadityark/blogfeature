from django  import forms
from questans.models  import Questions,Answers,QuestionGroups
from django.contrib.auth.models import User
class QuestionForm(forms.ModelForm):
    class Meta():
        model = Questions
        fields = ('title','group','slug')
        labels={
            "slug":"Body"
        }

class AnswerForm(forms.ModelForm):
    # question=forms.CharField(widget=forms.HiddenInput())
    class Meta():
        model = Answers
        fields =('answer_text',)
        # widgets = {'question': forms.HiddenInput()}
        
