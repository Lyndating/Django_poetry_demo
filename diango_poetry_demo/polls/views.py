from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world. your are at the polls index')

# we need to map the view to a URL (URLconf)