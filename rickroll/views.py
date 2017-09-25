import base58
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .forms import LinkForm
from .models import Link


def create_new(request):
    if request.method == 'POST':
        form = LinkForm(request.POST, request.FILES)
        if form.is_valid():
            link = form.save()
            return redirect(link.get_preview_url())
    else:
        form = LinkForm()

    return render(request, 'create_new.html', {
        'form': form,
    })


def link_view(request, id_str):
    try:
        id_int = base58.b58decode_int(id_str)
    except ValueError:
        raise Http404
    link = get_object_or_404(Link, id=id_int)
    return render(request, 'link_view.html', {
        'link': link,
    })


def preview(request, id_str):
    try:
        id_int = base58.b58decode_int(id_str)
    except ValueError:
        raise Http404
    link = get_object_or_404(Link, id=id_int)
    return render(request, 'preview.html', {
        'link': link,
    })
