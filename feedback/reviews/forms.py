from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     full_name = forms.CharField(label="Your full name", max_length=100, error_messages={
#                                 "required": "Your full name must not be empty",
#                                 "max_length": "Please enter a shorter full name"})
#     review_text = forms.CharField(label="Your feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['full_name', 'review_text', 'rating']

        labels = {
            "full_name": "Your full name",
            "review_text": "Your feedback",
            "rating": "Your rating"
        }

        error_messages = {
            "user_name":{
                "required":"Your full name is required",
                "max_length": "Please enter a shorter full name"
            }
        }

    # **IF you want all the fields
        # fields = '__all__'

    # **IF you want to specify the excluded fields
        # exclude = ['owner_comment']
