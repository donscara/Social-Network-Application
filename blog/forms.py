from django import forms
from django.utils.translation import gettext_lazy as _

# internals
from .models import Post


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = _('Body')

    class Meta:
        model = Post
        fields = ('body',)


class SearchForm(forms.Form):
    query = forms.CharField()
