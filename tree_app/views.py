from django.shortcuts import render


def mainpage(request):
    return render(request, 'tree_app/main.html')