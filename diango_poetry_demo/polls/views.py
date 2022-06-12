from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # indices from 0 to 4
    output = ", ".join([q.question_text for q in latest_question_list])
    # for...in loop through the array and 
    # convert array to string with , seperated
    return HttpResponse(output)

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