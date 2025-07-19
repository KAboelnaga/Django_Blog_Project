from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import ForbiddenWord
from .forms import ForbiddenWordsForm
from django.contrib import messages
#  Get all forbidden words
def forbidden_words_list(request):
    words = ForbiddenWord.objects.all()
    return render(request, 'forbidden/forbidden_words_list.html', {'words': words})


#  Add a new forbidden word

def add_forbidden_word(request):
    form = ForbiddenWordsForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        word = request.POST.get('word').strip().lower()
        if word:
            ForbiddenWord.objects.get_or_create(word=word)
            messages.success(request, "Forbidden word added successfully!")
            return redirect('forbidden:forbidden_words_list')
    return render(request, 'forbidden/add_forbidden_word.html')


#  Edit a forbidden word
def edit_forbidden_word(request, pk):
    word_instance = get_object_or_404(ForbiddenWord, pk=pk)
    if request.method == "POST":
        new_word = request.POST.get('word').strip()
        if new_word:
            word_instance.word = new_word
            word_instance.save()
            return redirect('forbidden:forbidden_words_list')
    return render(request, 'forbidden/edit_forbidden_word.html', {'word': word_instance})


#  Delete a forbidden word
def delete_forbidden_word(request, pk):
    word_instance = get_object_or_404(ForbiddenWord, pk=pk)
    word_instance.delete()
    return redirect('forbidden:forbidden_words_list')
