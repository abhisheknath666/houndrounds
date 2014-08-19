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

from houndroundsapp.models import Person, PetOwner, Walker

def index(request):
    return HttpResponseRedirect("http://houndrounds.com/houndrounds/signup")

def create_walker(name,email,walker_frequency, walker_schedule):
    try:
        person, created = Person.objects.get_or_create(email=email, name=name)
        walker, created = Walker.objects.get_or_create(person=person, defaults={'frequency':walker_frequency,
                                                                   'schedule':walker_schedule})
        return Walker
    except Exception as e:
        print str(e)
    return None

def create_owner(name,email,access,owner_frequency,owner_schedule):
    try:
        person,created = Person.objects.get_or_create(email=email, name=name)
        owner,created = PetOwner.objects.get_or_create(person=person, defaults={'pet_access':access,
                                                                  'frequency':owner_frequency,
                                                                  'schedule':owner_schedule})
        return owner
    except Exception as e:
        print str(e)
    return None

@csrf_exempt
def signup(request):
    if request.method=='POST':
        print str(request.POST)
        email = request.POST.get("email","guest@guest.com")
        name = request.POST.get("name", "guest")
        walker_schedule = request.POST.get("walker_schedule","")
        walker_frequency = request.POST.get("walker_frequency","")
        owner_schedule = request.POST.get("owner_schedule","")
        owner_frequency = request.POST.get("owner_frequency","")        
        access = request.POST.get("access","")
        redirect_url = reverse('thankyou')
        success = True
        if walker_schedule!="":
            walker = create_walker(name,email,walker_frequency, walker_schedule)            
            success = success or (walker!=None)
            print "Walker",walker
        if owner_schedule!="":
            owner = create_owner(name,email,access,owner_frequency,owner_schedule)
            success = success or (owner!=None)
            print "Owner",owner
        if not success:
            return HttpResponse("failed")
        return HttpResponseRedirect(redirect_url)
    context = {}
    return render(request, 'houndroundsapp/index.html', context)

@csrf_exempt
def thankyou(request):
    return render(request, 'houndroundsapp/thankyou.html')
