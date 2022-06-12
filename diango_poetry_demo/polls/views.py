from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # indices from 0 to 4, order by reverse way using "-" before the column name

    # template = loader.get_template('polls/index.html')
    context = {
        "latest_question_list": latest_question_list,
    }
    # load the template under html file and pass it a context dictionary. 
    # return HttpResponse(template.render(context, request))
    
    return render(request, "polls/index.html", context)

# we need to map the view to a URL (URLconf)

# a "type" of web apge that serves a specific funtion and has specific template.
# they take an argument
def detail(request, question_id):
    #print (request): <WSGIRequest: GET '/polls/1/'>
    return HttpResponse("You are looking at question %s." % question_id)
    # %s operator let you add value into python string. the value after the % sign will be replaced to that place.

def results(request, question_id):
    response ="You are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)