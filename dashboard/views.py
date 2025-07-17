from django.shortcuts import render, redirect
from forbidden.models import ForbiddenWord
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test


def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def dashboard_home(request):
    return render(request, 'dashboard/index.html')

@login_required
@user_passes_test(is_admin)
def forbidden_words_list(request):
    words = ForbiddenWord.objects.all()
    return render(request, 'dashboard/forbidden_words_list.html', {'words': words})

@login_required
@user_passes_test(is_admin)
def add_forbidden_word(request):
    if request.method == 'POST':
        word = request.POST.get('word', '').strip()
        if word:
            if ForbiddenWord.objects.filter(word__iexact=word).exists():
                messages.warning(request, "الكلمة موجودة بالفعل.")
            else:
                ForbiddenWord.objects.create(word=word)
                messages.success(request, "تمت إضافة الكلمة.")
        return redirect('forbidden_words_list')
    return render(request, 'dashboard/add_forbidden_word.html')

@login_required
@user_passes_test(is_admin)
def delete_forbidden_word(request, word_id):
    word = ForbiddenWord.objects.get(id=word_id)
    word.delete()
    messages.success(request, "تم حذف الكلمة.")
    return redirect('forbidden_words_list')