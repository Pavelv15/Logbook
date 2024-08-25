from django import forms

from .models import Topic, Entry

class TopicFrom(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widget = {'text':forms.Textarea(attrs={'cols':80})}#преобразования виджета
        

class SearchEntry(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}