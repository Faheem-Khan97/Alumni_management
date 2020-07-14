from django import forms
from .models import BlogPost, Files_Of_posts, Comment, Event



class DateInput(forms.DateInput):
    input_type = 'date'



class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','body']


class BlogPostWithFilesForm(BlogPostForm):

    files = forms.FileField(required = False, widget = forms.ClearableFileInput(attrs = {'multiple' : True}))
    fields = BlogPostForm.Meta.fields + ['files',]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment',]


class EventCreationForm(forms.ModelForm):
    event_date = forms.DateTimeField(
        
        input_formats = ['%Y-%m-%dT%H:%M'],
        widget = forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                },
            format='%Y-%m-%dT%H:%M')
    )
     
    class Meta:
        model = Event
        fields = ['event_name', 'event_details', 'venue', 'event_date',]




