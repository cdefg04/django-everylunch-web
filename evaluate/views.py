from django.contrib.auth.decorators import login_required
from django.core.mail import message
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from evaluate.forms import EvaluateForm
from evaluate.models import Evaluate


@login_required
def list(request):
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    evaluates = Evaluate.objects.all().order_by('-id')
    # list = Notice.objects.order_by('-id')

    # 페이징처리
    paginator = Paginator(evaluates, 5)  # 페이지당 5개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'evaluates': page_obj}
    return render(request, 'evaluate/evaluate_list.html', context)


@login_required
def write(request):
    if request.method == "POST":
        form = EvaluateForm(request.POST)

        if form.is_valid():
            evaluate = form.save(commit=False)
            evaluate.time = form.cleaned_data['time']
            evaluate.cafeteria = form.cleaned_data['cafeteria']
            evaluate.menu = form.cleaned_data['menu']
            evaluate.contents = form.cleaned_data['contents']
            evaluate.save()
            return redirect('/evaluate/list/')

    else:
        form = EvaluateForm()

    return render(request, 'evaluate/evaluate_write.html', {'form': form})


@login_required
def detail(request, pk):
    evaluate = Evaluate.objects.get(pk=pk)
    # pk 에 해당하는 글을 가지고 올 수 있게 된다.

    return render(request, 'evaluate/evaluate_detail.html', {'evaluate': evaluate})


@login_required
def delete(request, pk):
    evaluate = Evaluate.objects.get(pk=pk)

    evaluate.delete()
    return redirect('evaluate:list')
