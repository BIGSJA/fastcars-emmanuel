from typing import Any
from django import forms
from django.contrib.auth.models import User
from account.models import Profile

# ================== USER UPDATE FORM ===================
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email')

        
        def __init__(self, *args: Any, **kwargs: Any) -> None:
            super(UserUpdateForm, self).__init__(*args, **kwargs)

            for fieldname in ('first_name','last_name', 'username', 'email'):
                self.fields[fieldname].help_text = None

# ================== PROFILE UPDATE FORM =================
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',) 