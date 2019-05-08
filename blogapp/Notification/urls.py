from django.conf.urls import url
from django.urls import path
from Notification import views

app_name='Notification'

urlpatterns=[
   
    path('delete_notification/<int:pk>/notification/', views.delete_notification, name='delete_notification'),

   

    

]