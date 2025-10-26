from django.shortcuts import render
from django.http import HttpResponse

def faculty_home(request):
    return render(request,'faculty/faculty_home.html')
