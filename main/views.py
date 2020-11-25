from django.shortcuts import render


def list(request):
    return render(request, 'main/list.html')

