from django.shortcuts import render
from blogcontent.form import ArticleForm,CommentForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from blogcontent.models import Article,Comment
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.db.models import Q
from django.apps import apps



@login_required
def add_article(request):
    
    if request.method == 'POST':
        add_article_form = ArticleForm(data=request.POST)
        user = User.objects.get(id=request.user.id)
        if add_article_form.is_valid():                       
            a ={
                'author': user,
                'title' : add_article_form.cleaned_data['title'],
                'text'  : add_article_form.cleaned_data['text']              
            }
            a_insert = Article(**a) 
            a_insert.save()
            a_insert.publish()
            


    else:
        add_article_form = ArticleForm()
    return render(request,'blogcontent/add_blog.html',  {'article_form':add_article_form})

def view_blog(request):
    return render(request,'blogcontent/main.html')

def post_list(request):
    posts = Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blogcontent/post_list.html', {'posts': posts})

def post_edit(request, pk):
    post = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

    else:
        form = ArticleForm(instance=post)   
    return render(request, 'blogcontent/post_edit.html', {'form': form})

def post_remove(request, pk):
    post = get_object_or_404(Article, pk=pk)
    post.delete()
#    return redirect('post_list')

def post_detail(request, pk):
    blogdata = get_object_or_404(Article, pk=pk)
    return render(request, 'blogcontent/post_detail.html', {'blogdata': blogdata})

def add_comment_to_post(request, pk):
    post = get_object_or_404(Article, pk=pk)
    article = Article.objects.get(pk=pk)
    Notification = apps.get_model('Notification', 'Notification')
    a={
        'user':article.author,
        'title':'Commented to your post',
        'message':request.user.username+' is  commented on your post',
        'viewed':False
    }
    if request.method == "POST":        
        form = CommentForm(request.POST)
        if form.is_valid():
            a_insert = Notification(**a) 
            a_insert.save()
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('/', pk=post.pk)
    else:
        form = CommentForm()   
        return render(request, 'blogcontent/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('/', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('/', pk=comment.post.pk)

def search_content(request):
    if request.method == 'POST':
        search_word = request.POST['search']
        posts = Article.objects.filter(Q(title__contains=search_word) | Q(text__contains=search_word) | Q(catagory__contains=search_word) )
        return render(request, 'blogcontent/post_list.html', {'posts': posts})
        
     