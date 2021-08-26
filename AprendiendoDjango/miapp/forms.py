from django import forms
from django.forms.forms import Form
from django.forms.widgets import Widget
from django.core import validators


class FormArticle(forms.Form):

    title = forms.CharField(
        label="Titulo",
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': "Titulo del Archivo",
                'class': 'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'El titulo es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9ñ ]*$', 'El titulo no puede llevar caracteres especiales', 'invalid_title')
        ]
    )

    content = forms.CharField(
        label="Contenido",
        widget=forms.Textarea,
        validators=[
            validators.MaxLengthValidator(30, 'Demasiado texto')
        ]
    )
    content.widget.attrs.update({
        'placeholder': "Titulo del Archivo extenso",
        'class': 'titulo_form_article',
        'id': 'contenido_form'
    })

    public_options = [
        (1, 'Si'),
        (0, 'No')
    ]


    public = forms.TypedChoiceField(
        label = "¿Publicado?",
        choices = public_options
    )
