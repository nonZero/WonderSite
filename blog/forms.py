from django import forms
from blog import models


class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    content = forms.CharField(widget=forms.Textarea)
    years_of_experience = forms.IntegerField()
    feedback_type = forms.ChoiceField(
        choices=(
            (1, 'Site issue'),
            (2, 'Thank you'),
            (3, 'Question'),
        )
    )


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        exclude = (
            'user',
        )

