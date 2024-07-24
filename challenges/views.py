from multiprocessing import reduction
from urllib import response
from django import http
from django.http import HttpResponse ,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse






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
  "december":"year ends here",
}

# Create your views here.
# def janaury(request):
#   return HttpResponse("No meat for this months!")

# def feburary(request):
#   return HttpResponse("should walk 20 min every morning")

# def march(request):
#   return HttpResponse("should learn python every 20 mins a day")

def index(request):
  list_item = ""
  months = list(monthly_challenge.keys())
  
  for month in months:
    capitalized_month = month.capitalize()
    month_path = reverse("month_challenge",args=[month])
    list_item += f"<li><a href = \"{month_path}\">{capitalized_month}</a> </li>"
    
  response_data = f"<ul>{list_item}</ul>"
  return HttpResponse(response_data)

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
    response_data = f"<h1>{challenge_text}</h1>"
    return HttpResponse(response_data)
  except:
    return HttpResponseNotFound("this is not valid months")
 
    
  # if month == "janaury":
  #   challenge_text = ("No meat for this months!")
  # elif month == "feburary":
  #   challenge_text = ("should walk 20 min every morning")
  # elif month == "march":
  #   challenge_text = ("should learn python every 20 mins a day")

 