from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from os import mkdir
from .models import UserPicture
from todonoteapp.models import UserNote

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        npass = request.POST['npassword']
        cpass = request.POST['cpassword']
        user = User.objects.create_user(
            username = username,
            email = email,
            first_name = fname,
            last_name = lname
        )
        user.set_password(cpass)
        user.save()
        user = User.objects.get(username = username)
        uid = user.id
        UserPicture.objects.create(user_id = uid, picpath = '').save() 
        UserNote.objects.create(user_id = uid, note = 'Empty').save()
        mkdir(settings.MEDIA_ROOT + '/' + str(uid))
        mkdir(settings.MEDIA_ROOT + '/' + str(uid) + '/profile')
        mkdir(settings.MEDIA_ROOT + '/' + str(uid) + '/workspace')
        return redirect('/signin/')
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('../dashboard/' + str(user.id))
    return render(request, 'signin.html')

def signout(request):
    logout(request)
    return redirect('/')