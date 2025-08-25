# D:\gitRepos\website\djangoBckEnd\webdev\websiteDev\fetchStats\views.py
from django.shortcuts import render

def index(request):
    # Now points to fetchStats/templates/fetchStats/index.html
    return render(request, 'fetchStats/index.html')