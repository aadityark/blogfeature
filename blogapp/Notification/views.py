from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from Notification.models import Notification


# Create your views here.
def show_notification(request,notification_id):
    n= Notification.objects.get(id=notification_id)
    return render_to_response('notification/notification.html',{'notification':n})

def delete_notification(request,pk):
    n= Notification.objects.get(id=pk)
    n.viewed = True
    n.save()
    return HttpResponseRedirect('/')   