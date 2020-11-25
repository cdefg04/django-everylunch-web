from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .models import Notice
from .forms import NoticeForm
from django.contrib.auth.decorators import login_required

from django.db.models import Q


@login_required
def list(request):
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    notices = Notice.objects.order_by('-id')

    # 페이징처리
    paginator = Paginator(notices, 5)  # 페이지당 5개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'notices': page_obj, 'page': page}
    return render(request, 'notice/notice_list.html', context)


@login_required
def write(request):
    if request.method == "POST":
        form = NoticeForm(request.POST)

        if form.is_valid():
            notice = form.save(commit=False)
            notice.title = form.cleaned_data['title']
            notice.contents = form.cleaned_data['contents']
            notice.writer = request.user
            notice.save()
            return redirect('/notice/list/')

    else:
        form = NoticeForm()

    return render(request, 'notice/notice_write.html', {'form': form})


@login_required
def detail(request, pk):
    notice = Notice.objects.get(pk=pk)
    # pk 에 해당하는 글을 가지고 올 수 있게 된다.

    return render(request, 'notice/notice_detail.html', {'notice': notice})
    # {'notice':notice} 로 템플릿에 전달해 준다.


@login_required
def modify(request, pk):
    notice = Notice.objects.get(pk=pk)

    if request.user != notice.writer:
        message.error(request, '수정권한이 없습니다.')
        return redirect('notice:detail', pk=pk)

    if request.method == 'POST':
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.writer = request.user
            notice.save()
            return redirect('notice:detail', pk=pk)
    else:
        form = NoticeForm(instance=notice)
    context = {'form':form}
    return render(request, 'notice/notice_write.html', context)


@login_required
def delete(request, pk):
    notice = Notice.objects.get(pk=pk)

    if request.user != notice.writer:
        message.error(request, '삭제권한이 없습니다.')
        return redirect('notice:detail', pk=pk)

    notice.delete()
    return redirect('notice:list')