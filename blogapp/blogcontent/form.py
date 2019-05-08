#blogcontent/form
from django  import forms
from blogcontent.models  import Article
from .models import Comment
from django.contrib.auth.models import User
class ArticleForm(forms.ModelForm):
    # title=forms.CharField(label='Title', max_length=100)
    # content=forms.CharField(label='Content',widget=forms.Textarea)
    # CHOICES = (
    # ('health', 'Health & Fitness for Busy People'),
    # ('social_dynamic', 'Social Dynamics & Communication Skills'),
    # ('photogarphy','Point and Shoot Photography'),
    # ('food','Food'),
    # ('flower','Flower')
    # )
    # catagory = forms.ChoiceField(choices=CHOICES)
    # OPTIONS =(
    # ('tag1','Tag1'),
    # ('tag2','Tag2'),
    # ('tag3','Tag3'),
    # ('tag4','Tag4'),
    # ('tag5','Tag5')
    # )
    # tags = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=OPTIONS)
    class Meta():
        model = Article
        fields = ('title','text','catagory')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
    

    

       