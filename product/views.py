from django.http import HttpResponse

# from django.shortcuts import render

# request -> responses
# This is a request handler, not a viewer


def say_hello(request):
    return HttpResponse("hello world")
