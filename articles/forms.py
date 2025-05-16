from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'summary', 'body', 'document']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Field('title', css_class='form-control'),
            Field('summary', css_class='form-control'),
            Field('body', css_class='form-control'),
            # Field('photo', css_class='form-control'),
            Submit('submit', 'Saqlash', css_class='btn btn-primary')
        )