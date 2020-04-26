# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render

from .forms import SnippetForm
from .models import Snippet


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
