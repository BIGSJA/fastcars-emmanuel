from django import forms
from .models import Testimonial, Subscription

# ================== TESTIMONIAL FORM ================
class TestimonialForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'placeholder': "What's On Your Mind"}))
    class Meta:
        model = Testimonial
        fields = ('description',)     