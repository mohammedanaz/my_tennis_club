from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from members.models import Members
from datetime import datetime

def members(request):
  members_dict = {
    'members_key' : Members.objects.all().values(),
    'current_date' : datetime.now(),
    'is_even_minute' : datetime.now().minute % 2 == 0,
    'even_minute' : datetime.now().minute,
  }
  template = loader.get_template('all_members.html')
  return HttpResponse(template.render(members_dict, request))

def details(request, id):
  details_dict = {
    'one_member' : Members.objects.get(id = id),
    'current_date' : datetime.now(),
  }
  template = loader.get_template('details.html')
  return HttpResponse(template.render(details_dict, request))

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())