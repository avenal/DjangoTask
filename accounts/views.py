from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.template import loader

from .models import CustomUser

def index(request):
    users = CustomUser.objects.all()
    context = {
        "users": users
    }
    return render(request, 'accounts/index.html', context)

def user(request, id):
    user = get_object_or_404(CustomUser, id=id)
    context = {
        "user": user
    }
    return render(request, "accounts/user.html", context)

def add_user(request):
    if request.method == 'POST':
        # get form values
        birth_date = request.POST['birth_date']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # check if password match
        if password == password2:
           # check username
            if CustomUser.objects.filter(username=username).exists():
               messages.error(request, 'Username already taken')
               return redirect('add_user')
            else:
                if CustomUser.objects.filter(email=email).exists():
                    messages.error(request, 'E-mail already taken')
                    return redirect('add_user')
                else:
                    user = CustomUser.objects.create_user(username=username, password=password, email=email, birth_date=birth_date)
                    user.save()
                    messages.success(request, 'Success')
                    return redirect('index')
        else:
           #message
           messages.error(request, 'Passwords do not match')
           return redirect('add_user')
    else:    
        return render(request, 'accounts/add_user.html')

def edit_user(request, id):
    user = get_object_or_404(CustomUser, id=id)
    context = {
        "user": user
    }
    if request.method == 'POST':
        birth_date = request.POST['birth_date']
        username = request.POST['username']
        email = request.POST['email']
        number = request.POST['number']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
           # check username
            if CustomUser.objects.filter(username=username).exclude(id=user.id).exists():
               messages.error(request, 'Username already taken')
               return redirect('edit_user', id=id)
            else:
                if CustomUser.objects.filter(email=email).exclude(id=user.id).exists():
                    messages.error(request, 'E-mail already taken')
                    return redirect('edit_user', id=id)
                else:
                    user.username = username
                    user.email = email
                    user.number = number
                    user.set_password(password)
                    user.birth_date = birth_date
                    user.save()
                    messages.success(request, 'Success')
                    return redirect('index')
        else:
           #message
           messages.error(request, 'Passwords do not match')
           return redirect('edit_user', id=id)
    else:    
        return render(request, 'accounts/edit_user.html', context)

def delete_user(request, id):
    user = get_object_or_404(CustomUser, id=id)
    user.delete()
    messages.success(request, 'User deleted')

    return redirect('index')

def generate_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'
    data = CustomUser.objects.all()

    t = loader.get_template('csvtemplate.txt')
    c = {'data': data}
    response.write(t.render(c))
    return response
