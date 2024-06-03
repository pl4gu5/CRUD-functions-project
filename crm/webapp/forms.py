from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Record, Project
# Register a user

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# Login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())



# Create record form
class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']
        
# Update record form
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city',
                  'province', 'country'
                  ]

# Create project form
class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project', 'project_discription', 'project_cost', 'project_start_date',
                  'project_deadLine', 'employee_name', 'employee_email'
                  ]

# UpdaTe project form
class UpdateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project', 'project_discription', 'project_cost', 'project_start_date', 'project_deadLine', 'employee_name', 'employee_email']