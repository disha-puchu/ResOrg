from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from os import mkdir, remove
from shutil import move, rmtree
from authapp.models import UserPicture
from topicapp.models import TopicResource

@login_required(login_url='/signin/')
def profile(request, uid):
    profile_info = {}
    picpath = UserPicture.objects.get(user_id = uid).picpath
    return render(request, 'profile.html', {'profile_picpath' : picpath})

# Account Utils
@login_required(login_url='/signin/')
def editprofile(request, uid):
    if request.method == 'POST':           
        user = User.objects.get(id = uid)
        userpic = UserPicture.objects.get(user_id = uid)
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        picpath = ''
        if len(request.FILES) != 0:
            picpath = request.FILES['picture']
            userpic.picpath = picpath
            userpic.save()
        user.first_name = fname
        user.last_name = lname
        user.email = email
        user.save()
        if len(picpath) > 0:
            rmtree(settings.MEDIA_ROOT + '/' + str(uid) + '/profile')
            mkdir(settings.MEDIA_ROOT + '/' + str(uid) + '/profile')
            move(settings.MEDIA_ROOT + '/' + str(picpath), settings.MEDIA_ROOT + '/' + str(uid) + '/profile')
        return redirect('/dashboard/' + str(uid) + '/profile/')

@login_required(login_url='/signin/')
def changepassword(request, uid):
    if request.method == 'POST':
        opass = request.POST['opass']
        npass = request.POST['npass']
        cpass = request.POST['cpass']
        user = User.objects.get(id = uid)
        user.set_password(cpass)
        user.save()
        return redirect('/dashboard')
    
@login_required(login_url='/signin/')
def deleteaccount(request, uid):
    user = User.objects.get(id=uid)
    res_list = TopicResource.objects.filter(user_id = uid).values_list('rvalue')
    for res in res_list:
        if res not in ('weblink', 'ytlink'):
            remove(settings.MEDIA_ROOT + '/' + str(uid) + '/workspace/' + res[0])
    user.delete()
    rmtree(settings.MEDIA_ROOT + '/' + str(uid))
    return redirect('/')