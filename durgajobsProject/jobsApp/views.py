from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hydjobs(request):
    jobsinfo ="Hyderabad Jobs Information"
    return HttpResponse(jobsinfo)

def bangalorejobs(request):
    jobsinfo ="Bangalore Jobs Information"
    return HttpResponse(jobsinfo)

def chennaijobs(request):
    jobsinfo ="Chennai Jobs Information"
    return HttpResponse(jobsinfo)

def punejobs(request):
    jobsinfo ="Pune Jobs Information"
    return HttpResponse(jobsinfo)
