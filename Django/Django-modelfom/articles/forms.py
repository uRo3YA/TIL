from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "image"]
        labels = {"title": "제목", "content": "내용"}
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "제목을 입력해주세요"}
            ),
            "content": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "내용을 입력해주세요"}
            ),
        }
