from django.http import HttpResponse
from django.shortcuts import render

from posts.forms import SelectPostFromAuthor
from posts.models import Author
from django.template.loader import render_to_string


def htmx_form(request):
    form = SelectPostFromAuthor(context={})
    return render(request, "from.html", {"form": form})




def htmx_models(request):
    form = SelectPostFromAuthor(context=request.GET, initial={**request.GET})
    form_html = render_to_string("form_only.html", {"form": form}, request=request)
    return HttpResponse(form_html)
