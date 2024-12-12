from django.shortcuts import render
from django.http import HttpResponse


# this fun for http response
def post_list_view(request):
    return HttpResponse("ok")

