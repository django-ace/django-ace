from .forms import SnippetForm, VimSnippetForm
from .models import Snippet
from django.shortcuts import render, redirect


def simple(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        vim_form = VimSnippetForm()
        if 'submit_standard' in request.POST and form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SnippetForm()
        vim_form = VimSnippetForm()
    
    return render(request, "snippets.html", {
        "form": form,
        "vim_form": vim_form,
        "snippets": Snippet.objects.all()
    })
