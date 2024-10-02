from .models import Comment , Post
from django import forms 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['name', 'email', 'body']
        
class SearchForm(forms.Form):
    query = forms.CharField()

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','slug', 'body', 'status', 'tags']