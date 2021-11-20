from django import forms
from .models import Post
from .widgets import ImageFieldAdminCustomWidget


class PostAdminModelForm(forms.ModelForm):
    preview_image = forms.ImageField(widget=ImageFieldAdminCustomWidget())
    class Meta:
        model = Post
        fields = '__all__'