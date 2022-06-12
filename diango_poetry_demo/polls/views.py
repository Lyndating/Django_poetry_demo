from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world. your are at the polls index')

# we need to map the view to a URL (URLconf)

# a "type" of web apge that serves a specific funtion and has specific template.
# they take an argument
def detail(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id)
    # %s operator let you add value into python string. the value after the % sign will be replaced to that place.

def results(request, question_id):
    response ="You are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)