from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# import numpy as np
from itertools import combinations
import json

def Home(request):
    return render (request, 'Home.html')
