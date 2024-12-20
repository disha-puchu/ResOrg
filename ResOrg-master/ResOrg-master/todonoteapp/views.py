from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from todonoteapp.models import UserNote, UserTodo

def todo_create(request, uid):
    if request.method == 'POST':           
        todo = request.POST.get('todo')
        UserTodo.objects.create(
            user_id = uid,
            todo = todo,
            tick = 0
        ).save()

def todo_edit(request, uid, tdid):
    if request.method == 'POST':           
        todo = request.POST.get('todo')
        todoo = UserTodo.objects.get(tdid = tdid)
        todoo.todo = todo
        todoo.save()

def todo_check(request, uid, tdid):
    todoo = UserTodo.objects.get(tdid = tdid)
    if todoo.tick == 0:
        todoo.tick = 1
    else:
        todoo.tick = 0
    todoo.save()

def todo_delete(request, uid, tdid):
    UserTodo.objects.get(tdid = tdid).delete()

def note_edit(request, uid):
    if request.method == 'POST':           
        note = request.POST.get('note')
        if len(UserNote.objects.all()) > 0:
            UserNote.objects.filter(user_id = uid).update(note = note)
        else:
            UserNote.objects.create(
                user_id = uid,
                note = note
            ).save()

def note_clear(request, uid):
    UserNote.objects.filter(user_id = uid).update(note = 'Empty')

def re_dir(uid, tid):
    if tid == None:
        return redirect('/dashboard/' + str(uid) + '/')
    else:
        return redirect('/dashboard/' + str(uid) + '/topic/' + str(tid) + '/')

@login_required(login_url='/signin/')
def createtodo(request, uid, tid = None):
    todo_create(request, uid)
    return re_dir(uid, tid)

@login_required(login_url='/signin/')
def edittodo(request, uid, tdid, tid = None):
    todo_edit(request, uid, tdid)
    return re_dir(uid, tid)

@login_required(login_url='/signin/')
def checktodo(request, uid, tdid, tid = None):
    todo_check(request, uid, tdid)
    return re_dir(uid, tid)

@login_required(login_url='/signin/')
def deletetodo(request, uid, tdid, tid = None):
    todo_delete(request, uid, tdid)
    return re_dir(uid, tid)

@login_required(login_url='/signin/')
def editnote(request, uid, tid = None):
    note_edit(request, uid)
    return re_dir(uid, tid)

@login_required(login_url='/signin/')
def clearnote(request, uid, tid = None):
    note_clear(request, uid)
    return re_dir(uid, tid)