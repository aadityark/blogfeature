# dprojx/urls.py
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from blogauth import views
from blogcontent.views import add_article
from questans.views import add_question
from Notification.views import show_notification
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^writeplus/',include('blogauth.urls', namespace='blogauth')),
    url(r'^addblog/',include('blogcontent.urls', namespace='blogcontent')),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^questans/',include('questans.urls', namespace='questans')),
    url(r'^notification/',include('Notification.urls',namespace='notification'))
    

]