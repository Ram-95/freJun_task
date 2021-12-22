from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Welcome to FreJun API.")


def inbound(request):
    return HttpResponse("You are at INBOUND SMS Route.")


def outbound(request):
    return HttpResponse("You are at OUTBOUND SMS Route.")
