from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import ForbiddenWord


# ✅ Get all forbidden words
def forbidden_words_list(request):
    words = ForbiddenWord.objects.all()
    return render(request, 'forbidden/forbidden_words_list.html', {'words': words})


# ✅ Add a new forbidden word
@require_http_methods(["POST", "GET"])
def add_forbidden_word(request):
    if request.method == "POST":
        word = request.POST.get('word').strip()
        if word:
            ForbiddenWord.objects.get_or_create(word=word)
            return redirect('forbidden_words_list')
    return render(request, 'forbidden/add_forbidden_word.html')


# ✅ Edit a forbidden word
@require_http_methods(["POST", "GET"])
def edit_forbidden_word(request, pk):
    word_instance = get_object_or_404(ForbiddenWord, pk=pk)
    if request.method == "POST":
        new_word = request.POST.get('word').strip()
        if new_word:
            word_instance.word = new_word
            word_instance.save()
            return redirect('forbidden_words_list')
    return render(request, 'forbidden/edit_forbidden_word.html', {'word': word_instance})


# ✅ Delete a forbidden word
@require_http_methods(["POST"])
def delete_forbidden_word(request, pk):
    word_instance = get_object_or_404(ForbiddenWord, pk=pk)
    word_instance.delete()
    return redirect('forbidden_words_list')
