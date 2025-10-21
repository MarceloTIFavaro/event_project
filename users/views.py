from django.http import HttpResponse

def index(reques):
    return HttpResponse("Ola Users")