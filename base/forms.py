from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm
from base.models import User

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
