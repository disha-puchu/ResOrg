from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from os import mkdir
from shutil import move, rmtree
from os import remove
from authapp.models import UserPicture
from .models import UserGroup, GroupTopic
from topicapp.models import TopicResource
from todonoteapp.models import UserTodo, UserNote

@login_required(login_url='/signin/')
def dashboard(request, uid):
    picpath = UserPicture.objects.get(user_id = uid).picpath
    groups = UserGroup.objects.filter(user_id = uid).values_list('gid', 'gname', 'gdesc')
    todos = UserTodo.objects.filter(user_id = uid).values_list('tdid', 'todo', 'tick')
    notedata = UserNote.objects.filter(user_id = uid).values_list('note')
    group_list = {}
    topic_list = {}
    todo_list = {}
    for tdid, *rest in todos:
        todo_list[tdid] = rest
    for gid, *ginfo in groups:
        group_list[gid] = list(ginfo)
        topics_per_group = GroupTopic.objects.filter(group_id = gid).values_list('tid', 'tname', 'tdesc')
        topics_per_group_list = {}
        for tid, *tinfo in topics_per_group:
            topics_per_group_list[tid] = list(tinfo)
        topic_list[gid] = topics_per_group_list 
    # return render(request, 'dashboard.html', {'picpath' : picpath, 'group_list' : group_list, 'topic_list' : topic_list})
    return render(request, 'dashboard_t.html', {'picpath' : picpath, 'group_list' : group_list, 'topic_list' : topic_list, 'todo_list' : todo_list, 'notedata' : notedata[0]})

# Group Utils
@login_required(login_url='/signin/')
def creategroup(request, uid):
    if request.method == 'POST':           
        name = request.POST['name']
        desc = request.POST['desc']
        UserGroup.objects.create(
            user_id = uid,
            gname = name,
            gdesc = desc
        ).save()
        return redirect('/dashboard/' + str(uid) + '/')
    return redirect('/')

@login_required(login_url='/signin/')
def renamegroup(request, uid, gid):
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        group = UserGroup.objects.get(gid = gid)
        group.gname = name
        group.gdesc = desc
        group.save()
    return redirect('/dashboard/' + str(uid) + '/')

@login_required(login_url='/signin/')
def deletegroup(request, uid, gid):
    res_list = TopicResource.objects.filter(user_id = uid, group_id = gid).values_list('rvalue')
    for res in res_list:
        if res not in ('weblink', 'ytlink'):
            remove(settings.MEDIA_ROOT + '/' + str(uid) + '/workspace/' + res[0])
    UserGroup.objects.get(gid = gid, user_id = uid).delete()
    return redirect('/dashboard/' + str(uid) + '/')

# Topic Utils
@login_required(login_url='/signin/')
def createtopic(request, uid):
    if request.method == 'POST':           
        name = request.POST['name']
        gid = request.POST['gid']
        desc = request.POST['desc']
        GroupTopic.objects.create(
            tname = name,
            tdesc = desc,
            group_id = gid,
            user_id = uid
        ).save()
        return redirect('/dashboard/' + str(uid) + '/')
    return redirect('/')

@login_required(login_url='/signin/')
def renametopic(request, uid, gid, tid):
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        topic = GroupTopic.objects.get(user_id = uid, group_id = gid, tid = tid)
        topic.tname = name
        topic.tdesc = desc
        topic.save()
    return redirect('/dashboard/' + str(uid) + '/')

@login_required(login_url='/signin/')
def deletetopic(request, uid, gid, tid):
    res_list = TopicResource.objects.filter(user_id = uid, group_id = gid, topic_id = tid).values_list('rvalue')
    for res in res_list:
        if res not in ('weblink', 'ytlink'):
            remove(settings.MEDIA_ROOT + '/' + str(uid) + '/workspace/' + res[0])
    GroupTopic.objects.get(tid = tid, group_id = gid, user_id = uid).delete()
    return redirect('/dashboard/' + str(uid) + '/')