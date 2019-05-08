from django.conf.urls import url
from questans import views
from django.urls import path

app_name='questans'

urlpatterns=[
    url(r'^add_question/$',views.add_question,name='add_question'),
    path('answer/<int:pk>/question/', views.answer_question, name='answer_question'),
   

    

]