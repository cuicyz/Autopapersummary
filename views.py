from django.shortcuts import render
from django.shortcuts import HttpResponse
import logging
from gensim.summarization import summarize

# Create your views here.

summarization_list=[
    {"text":"Your summarization"},
]

def index(request):
    if request.method =="POST":
        summarization=request.POST.get("text",None)
        summarization=summarize(summarization)
        temp={"text":summarization}
        summarization_list.append(temp)
    return render(request,"index.html",{"data":summarization_list})
