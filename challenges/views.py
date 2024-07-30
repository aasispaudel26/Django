from multiprocessing import reduction
import re
from urllib import response
from django import http
from django.http import HttpResponse ,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

import challenges







monthly_challenge = {
  "janaury" :"No meat for this months!",
  "feburary":"should walk 20 min every morning",
  "march":"should learn python every 20 mins a day",
  "april":"should go on a tour",
  "may":"have exams",
  "june":"college starts",
  "july":"birthday months",
  "august":"summer slams",
  "september":"can eat meat",
  "october":"best months",
  "november":"cutest month",
  "december": "visit to village" ,
}

# Create your views here.
# def janaury(request):
#   return HttpResponse("No meat for this months!")

# def feburary(request):
#   return HttpResponse("should walk 20 min every morning")

# def march(request):
#   return HttpResponse("should learn python every 20 mins a day")

def index(request):
  months = list(monthly_challenge.keys())
  
  # for month in months:
  #  return render(request,"challenges/index.html",{
  #    "months" : months 
  #  })
  
  return render(request, 'challenges/index.html', context={'months':months})
 
 
 
def monthly_challenges_by_number(request, month):
  months = list(monthly_challenge.keys())
  if month > len(months):
    return HttpResponseNotFound("invalid months")
  redirect_month = months[month - 1]
  redirect_path = reverse("month_challenge",args=[redirect_month])
  return HttpResponseRedirect(redirect_path)

def monthly_challenges(request, month):
  try:
    challenge_text = monthly_challenge[month]
    return render(request,"challenges/challenges.html", {
      "text" : challenge_text,
      "months" : month
    })
  except:
    return HttpResponseNotFound("this is not valid months")
 
    
  
 