from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Alert
from django.template import RequestContext, loader
from alerts.forms import AlertForm
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth import authenticate, login

from django.core import serializers
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def active(request):
    
     if request.method == 'POST':
          form = AlertForm(request.POST)
          if form.is_valid():
               form.save()
     else:
          form = AlertForm()
     alert_list = Alert.objects.order_by('id')                
     output = loader.get_template('alerts/active.html')
     context = RequestContext(request, {
                    'alert_list' : alert_list,
                    'username' : request.user.username,
                                })
     return render(request,'alerts/active.html', {'form': form, 'alert_list' : alert_list, 'username' : request.user.username,})
     

def alert_json(request):
     alerts = Alert.objects.all()
     data = serializers.serialize("json", alerts)
     return HttpResponse(data, content_type='application/json')

'''     if request.method == "POST":
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(username = username, password = password)
          if user is not None:
               login(request, user)
               return redirect('alerts/active.html')
          else:
               return HttpResponse('<h1>Invalid username/password combination</h1>')
     else:
          return render(request, 'alerts/index.html')
     
def login_user(request):
     logout(request)
     username = password = ''
     if request.POST:
          username = request.POST['username']
          password = request.POST['password']

          user = authenticate(username=username, password=password)
          if user is not None:
               if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/active.html')
               return render_to_response('active.html', context_instance=RequestContext(request)) '''


def index(request):

     if request.user.is_authenticated():
          return redirect(reverse_lazy('active'))
     else:
          return redirect(reverse_lazy('login'))
  
