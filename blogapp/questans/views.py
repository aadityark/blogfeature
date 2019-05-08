from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.db.models import Q
from questans.models import Questions, Answers, QuestionGroups
from questans.form import QuestionForm,AnswerForm
from django.contrib.auth.models import User
from django.apps import apps
# Create your views here.

def add_question(request):
    questions = Questions.objects.all()
    if request.method == 'POST':
        add_question_form = QuestionForm(data=request.POST)
        if add_question_form.is_valid():
          add_question_form.save()
    else:
        add_question_form = QuestionForm()
    context = {'add_question_form':add_question_form, 'question_set':questions}    
    return render(request,'question_answer/add_question.html',  context)

def answer_question(request,pk):
    question = get_object_or_404(Questions, pk=pk)
    answers =  Answers.objects.filter(question = pk)
    user = User.objects.get(id=request.user.id)
    Notification = apps.get_model('Notification', 'Notification')
    n={
        'user':question.user,
        'title':'Answered to your question',
        'message':request.user.username+' is  answered to your question',
        'viewed':False
    }
    if request.method == 'POST':
        add_answer_form=AnswerForm(data=request.POST)
        if add_answer_form.is_valid():
            a = {
                'user':user,
                'question':question,
                'answer_text':add_answer_form.cleaned_data['answer_text']
                }
            a_insert = Answers(**a) 
            a_insert.save()
            n_insert = Notification(**n) 
            n_insert.save()
        else:
            print('Form is invalid')

       
    else:
         add_answer_form=AnswerForm()   
    
    return render(request, 'question_answer/answer_question.html', {'question': question,'answers':answers,'answer_form':add_answer_form})
   



