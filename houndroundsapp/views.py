from django.shortcuts import render
from django.template import Context, Template
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.core import exceptions
import json
import base64
import urllib

def index(request):
    return HttpResponseRedirect("http://houndrounds.com")

@csrf_exempt
def signup(request):
    #     form = None
    #     if request.method=='POST':        
    #         form = ListenerAvailabilityForm(request.POST)
    #         if form.is_valid():
    #             cleaned_data = form.cleaned_data
    #             availability = cleaned_data.get("availability",listener.enabled)
    #             listener.enabled = availability
    #             listener.busy = False
    #             listener.save()
    #     else:
    #         form = ListenerAvailabilityForm()
    #     availability_str = "unavailable"
    #     if listener.enabled:
    #         availability_str = "available"
    #     context = { 'listener' : listener, 
    #                 'total_minutes': str(total_minutes),
    #                 'unpaid_minutes' : str(unpaid_minutes),
    #                 'redirect_url' : str(redirect_url),
    #                 'availability' : availability_str,
    #                 'form' : form}
    #     return render(request, 'houndroundsapp/index.html', context)
    # except Exception as e:
    #     logger.debug("%s",str(e))
    #     raise Http404
    if request.method=='POST':
        print str(request.POST)
        email = request.POST.get("email","guest@guest.com")
        name = request.POST.get("name", "guest")
        schedule = request.POST.get("schedule","")
        frequency = request.POST.get("frequency","")
        access = request.POST.get("access","")
        print "Email: "+email+"\nName: "+name+"\nSchedule: "+schedule+"\nFrequency: "+frequency+"\nAccess: "+access
        return HttpResponse("success")
    context = {}
    return render(request, 'houndroundsapp/index.html', context)

