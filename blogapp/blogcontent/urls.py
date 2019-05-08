# dappx/urls.py
from django.conf.urls import url
from blogcontent import views
from django.urls import path

# SET THE NAMESPACE!
app_name = 'blogcontent'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^add_article/$',views.add_article,name='add_article'),
    url(r'^view_blog/$',views.view_blog,name='view_blog'),
    url(r'^post_listing/$',views.post_list,name='post_list'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    url(r'^search_content/$',views.search_content,name='search_content'),


    

]