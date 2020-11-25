from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from check.forms import CheckForm
from check.models import Check


@login_required
def list(request):
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    checks = Check.objects.order_by('-id')

    # 페이징처리
    paginator = Paginator(checks, 5)  # 페이지당 5개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'checks': page_obj, 'page': page}
    return render(request, 'check/check_list.html', context)


@login_required
def write(request):
    if request.method == "POST":
        form = CheckForm(request.POST)

        if form.is_valid():
            check = form.save(commit=False)
            check.time = form.cleaned_data['time']
            check.cafeteria = form.cleaned_data['cafeteria']
            check.menu = form.cleaned_data['menu']
            check.save()
            return redirect('/check/list/')

    else:
        form = CheckForm()

    return render(request, 'check/check_write.html', {'form': form})


@login_required
def detail(request, pk):
    check = Check.objects.get(pk=pk)
    # pk 에 해당하는 글을 가지고 올 수 있게 된다.

    return render(request, 'check/check_detail.html', {'check': check})
    # {'notice':notice} 로 템플릿에 전달해 준다.



@login_required
def modify(request, pk):
    check = Check.objects.get(pk=pk)

    if request.method == 'POST':
        form = CheckForm(request.POST, instance=check)
        if form.is_valid():
            check = form.save(commit=False)
            check.save()
            return redirect('check:detail', pk=pk)
    else:
        form = CheckForm(instance=check)
    context = {'form':form}
    return render(request, 'check/check_write.html', context)


@login_required
def delete(request, pk):
    check = Check.objects.get(pk=pk)

    check.delete()
    return redirect('check:list')
