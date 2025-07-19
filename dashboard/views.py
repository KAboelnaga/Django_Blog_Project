from django.shortcuts import render, redirect, get_object_or_404
from forbidden.models import ForbiddenWord
from django.contrib import messages
from forbidden.forms import ForbiddenWordsForm
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
def edit_forbidden_word(request, word_id):
    word = get_object_or_404(ForbiddenWord, id=word_id)
    form = ForbiddenWordsForm(request.POST or None, instance=word)
    if form.is_valid():
        form.save()
        messages.success(request, 'Forbidden word updated successfully!')
        return redirect('forbidden_words_list')
    return render(request, 'dashboard/edit_forbidden_word.html', {'form': form, 'word': word})

@login_required
@user_passes_test(is_admin)
def add_forbidden_word(request):
    if request.method == 'POST':
        form = ForbiddenWordsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Forbidden word added successfully!")
            return redirect('forbidden_words_list')
    else:
        form = ForbiddenWordsForm()
    return render(request, 'dashboard/add_forbidden_word.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def delete_forbidden_word(request, word_id):
    word = ForbiddenWord.objects.get(id=word_id)
    if request.method == 'POST':
        word.delete()
        messages.success(request, "Forbidden word deleted successfully!")
        return redirect('forbidden_words_list')
    return render(request, 'dashboard/delete_forbidden_word.html', {'word': word})
