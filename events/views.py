from django.http import HttpResponse

def index(reques):
    return HttpResponse("Olá, mundo. Este é o index de meu projeto sobre eventos")