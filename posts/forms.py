from django import forms
from django.forms import HiddenInput
from django.urls import reverse
from dynamic_forms import DynamicField, DynamicFormMixin

from posts.models import Author, Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Submit


def is_hidden(author, widget):
    return HiddenInput() if author == '2' else widget


class SelectPostFromAuthor(DynamicFormMixin, forms.Form):
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
    )
    blog = DynamicField(
        forms.ModelChoiceField,
        queryset=lambda form: Post.objects.filter(author=form.context["author"]),
    )
    notes = DynamicField(
        forms.CharField,
        widget=lambda form: is_hidden(form.context["author"], forms.Textarea)
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Field('author', css_class='form-control',
                      **{'hx-get': reverse('chained-author'), 'hx-target': '#form', 'hx-trigger': 'change',
                         'hx-swap': 'outerHTML'}),
                css_class='form-group'
            ),
            Div(
                Field('blog', css_class='form-control included', css_id='id_blog'),
                css_class='form-group'
            ),
            Div(
                Field('notes', css_class='form-control included', css_id='id_notes'),
            ),
        )
