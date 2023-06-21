from django import forms
from post.models import PostModel


class PostModelForm(forms.ModelForm):
	class Meta:
		model = PostModel
		fields = ('title', 'content', 'author')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'content': forms.TextInput(attrs={'class': 'form-control'}),
			'author': forms.TextInput(attrs={'class': 'form-control'}),
		}
		