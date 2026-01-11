from django import forms
from django.utils import timezone
from .models import Post, Comment
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    pub_date = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
            }
        ),
        label='Дата и время публикации',
        help_text='Оставьте пустым для публикации сейчас.'
    )

    class Meta:
        model = Post
        fields = ('title', 'text', 'pub_date', 'location', 'category', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        now_local = timezone.localtime(timezone.now())
        self.fields['pub_date'].widget.attrs['min'] = now_local.strftime('%Y-%m-%dT%H:%M')

    def clean_pub_date(self):
        return self.cleaned_data.get('pub_date') or timezone.now()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
