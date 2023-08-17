from django import forms
from django.forms import HiddenInput
from django.urls import reverse
from dynamic_forms import DynamicField, DynamicFormMixin

from posts.models import Author, Post, Comments
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Submit


def is_hidden(statement, widget):
    return widget if statement else HiddenInput()


class SelectPostFromAuthor(DynamicFormMixin, forms.Form):
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
    )
    post = DynamicField(
        forms.ModelChoiceField,
        queryset=lambda form: Post.objects.filter(author=form.context.get("author")),
        widget=lambda form: is_hidden(form.context.get("author"), forms.Select)

    )
    comments = DynamicField(
        forms.ModelChoiceField,
        queryset=lambda form: Comments.objects.filter(post=form.context.get("post")),
        widget=lambda form: is_hidden(form.context.get("post"), forms.Select)

    )
    notes = forms.CharField(

    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Field('author', css_class='form-control included',
                      **{'hx-get': reverse('form'), 'hx-target': '#form', 'hx-trigger': 'change',
                         'hx-swap': 'outerHTML'}),
                css_class='form-group'
            ),
            Div(
                Field('post', css_class='form-control', css_id='id_blog',
                      **{'hx-get': reverse('form'), 'hx-target': '#form', 'hx-trigger': 'change',
                         'hx-swap': 'outerHTML', 'hx-include':'.included'}
                      ),
                css_class='form-group'
            ),
            Div(
                Field('comments', css_class='form-control', css_id='id_comments'),
                css_class='form-group'
            ),

            Div(
                Field('notes', css_class='form-control', css_id='id_notes'),
            ),
        )
