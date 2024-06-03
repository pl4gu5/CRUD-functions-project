from django.shortcuts import render, redirect
from .forms import UserCreationForm, LoginForm, CreateRecordForm, CreateProjectForm, UpdateRecordForm, UpdateProjectForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from . models import Project, Record
from django.contrib import messages

# Home
def home(request):

    return render(request, 'webapp/index.html', {})

# Register a user

def Register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if  form.is_valid():
                form.save()
                messages.success(request, "Account Created Successfully | You can login now.")
                return redirect("login")
    context = {'form': form}
    return render(request, 'webapp/register.html', context)

# Login a user

def My_Login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
             username = request.POST.get('username')
             password = request.POST.get('password')
             user = authenticate(username=username, password=password)
             if user is not None:
                  auth.login(request, user)
                  return redirect("dashboard")
    context = {'form': form}
    return render(request, 'webapp/my-login.html', context)



# Dashboard
@login_required(login_url='login')
def dashboard(request):
     my_record = Record.objects.all()
     my_project = Project.objects.all()
     

     context = {'records': my_record, 'projects': my_project}
     return render(request, 'webapp/dashboard.html', context)

# Create a record
@login_required(login_url='login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == 'POST':
          form = CreateRecordForm(request.POST)
          if form.is_valid():
            form.save()
            messages.success(request, "Record Created Successfully")
            return redirect("dashboard")
    context = {'create_record_form': form}
    return render(request, 'webapp/create-record.html', context)



# Update a record
@login_required(login_url='login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':
       form = UpdateRecordForm(request.POST, instance=record)
       if form.is_valid():
            form.save()
            messages.success(request, "Record Updated Successfully")
            return redirect('dashboard')

    context = {'update_record_form': form, 'record': record}
    return render(request, 'webapp/update-record.html', context)

# View a record

@login_required(login_url='login')
def single_record(request, pk):
    view_record = Record.objects.get(id=pk)
    
    context = {'record': view_record}
    return render(request, 'webapp/view-record.html', context)

# Delete a record
@login_required(login_url='login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request, "Record Deleted Successfully")
    return redirect("dashboard")

# create a project
@login_required(login_url='login')
def create_project(request):
    form = CreateProjectForm()
    if request.method == 'POST':
         form = CreateProjectForm(request.POST)
         if form.is_valid():
            form.save()
            messages.success(request, "Project Created Successfully")
            return redirect("dashboard")
    context = {'create_project_form': form}
    return render(request, 'webapp/create-project.html', context)

# Update project
@login_required(login_url='login')
def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = UpdateProjectForm(instance=project)

    if request.method == 'POST':
       form = UpdateProjectForm(request.POST, instance=project)
       if form.is_valid():
            form.save()
            messages.success(request, "Project Updated Successfully")
            return redirect('dashboard')

    context = {'update_project_form': form, 'project': project}
    return render(request, 'webapp/update-project.html', context)

# View a project
@login_required(login_url='login')
def single_project(request, pk):
    view_project = Project.objects.get(id=pk)
    
    context = {'project': view_project}
    return render(request, 'webapp/view-project.html', context)

# Delete a project
@login_required(login_url='login')
def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()
    messages.success(request, "Project Deleted Successfully")
    return redirect('dashboard')

# User Logout
def user_logout(request):
    auth.logout(request)
    messages.success(request, "Logout Success! CYA soon")
    return redirect("login")