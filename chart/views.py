from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def list(request):
    return render(request, 'chart/chart_list.html')