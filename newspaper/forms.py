from django import forms
from newspaper.models import Contact, Newsletter, Comment


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        
