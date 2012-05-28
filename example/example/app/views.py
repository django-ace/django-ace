from .forms import SnippetForm
from .models import Snippet
from django.shortcuts import render, redirect


def simple(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SnippetForm()
    return render(request, "snippets.html", {
        "form": form,
        "snippets": Snippet.objects.all()
    })
