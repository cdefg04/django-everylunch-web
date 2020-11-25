from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from accounts.forms import JoinForm, CustomUserChangeForm, CustomPasswordChangeForm


def join(request):
    if request.method == "POST":
        form = JoinForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = JoinForm()
    return render(request, 'registration/join.html', {'form': form})


@login_required
def update(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)

        if user_change_form.is_valid():
            user_change_form.save()
            return redirect('/accounts/people/', request.user.username)

    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
        return render(request, 'registration/update.html', {'user_change_form': user_change_form})


@login_required
def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('/')
    return render(request, 'registration/delete.html')


@login_required
def password(request):
    password_change_form = CustomPasswordChangeForm(request.user, request.POST)
    if password_change_form.is_valid():
        user = password_change_form.save()
        update_session_auth_hash(request, user)
        messages.success(request, "비밀번호를 성공적으로 변경하였습니다.")
        return redirect('/')

    else:
        password_change_form = CustomPasswordChangeForm(request.user)

    return render(request, 'registration/password.html', {'password_change_form': password_change_form})
