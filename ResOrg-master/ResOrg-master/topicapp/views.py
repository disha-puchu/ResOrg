from shutil import move
from os import remove, rename
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import GroupTopic, TopicResource, TopicSection
from authapp.models import UserPicture
from todonoteapp.models import UserTodo, UserNote
from youtube_api import youtube_search

def get_ytvdo_id(url):
    yt_url = "https://www.youtube.com/embed/"
    pattern_1 = '/watch?v='
    pattern_2 = '/youtu.be/'
    in_1 = url.find(pattern_1)
    in_2 = url.find(pattern_2)
    end_in = 0
    vid = ''
    if in_1 == -1 and in_2 == -1:
        return url
    elif in_2 == -1:
        end_in = in_1 + len(pattern_1)
    else:
        end_in = in_2 + len(pattern_2)
    end_with_in = url.find('?', end_in)
    if end_with_in == -1:
        vid = url[end_in:]
    else:
        vid = url[end_in:end_with_in]
    url = yt_url + vid
    return url

@login_required(login_url='/signin/')
def topic(request, uid, tid, search_results = None):
    gid = GroupTopic.objects.get(tid = tid).group_id
    picpath = UserPicture.objects.get(user_id = uid).picpath
    topic_info = {
        'uid' : uid,
        'tid' : tid,
        'gid' : gid,
        'tname' : GroupTopic.objects.get(tid = tid).tname,
        'picpath' : picpath
    }
    todos = UserTodo.objects.filter(user_id = uid).values_list('tdid', 'todo', 'tick')
    notedata = UserNote.objects.filter(user_id = uid).values_list('note')
    resource_info = {}
    section_info = {}
    todo_list = {}
    for tdid, *rest in todos:
        todo_list[tdid] = rest
    section_list = TopicSection.objects.filter(topic_id = tid, group_id = gid, user_id = uid).values_list('sid', 'sname', 'sdesc')
    for sid, *sinfo in section_list:
        section_info[sid] = sinfo
        resource_info[sid] = {}
    resource_list = TopicResource.objects.filter(topic_id = tid).values_list('section_id', 'rid', 'rname', 'rvalue', 'rtype')
    for sid, rid, *rinfo in resource_list:
        resource_info[sid][rid] = rinfo
    return render(request, 'topic_t.html', {'topic_info' : topic_info, 'section_info' : section_info, 'resource_info' : resource_info, 'todo_list' : todo_list, 'notedata' : notedata[0]})
    # return render(request, 'topic_t.html', {'topic_info' : topic_info, 'section_info' : section_info, 'resource_info' : resource_info, 'search_results' : search_results})
    # return render(request, 'topic.html', {'topic_info' : topic_info, 'section_info' : section_info, 'resource_info' : resource_info})

# Section Utils
@login_required(login_url='/signin/')
def createsection(request, uid, tid):
    if request.method == 'POST':
        sname = request.POST['name']
        sdesc = request.POST['desc']
        gid = GroupTopic.objects.get(tid = tid).group_id
        TopicSection.objects.create(
            sname = sname,
            sdesc = sdesc,
            group_id = gid,
            topic_id = tid,
            user_id = uid
        ).save()
    return redirect('/dashboard/' + str(uid) + '/topic/' + str(tid) + '/')

@login_required(login_url='/signin/')
def renamesection(request, uid, tid, sid):
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        gid = GroupTopic.objects.get(tid = tid).group_id
        TopicSection.objects.filter(user_id = uid, group_id = gid, topic_id = tid, sid = sid).update(sname = name, sdesc = desc)
    return redirect('/dashboard/' + str(uid) + '/topic/' + str(tid) + '/')

@login_required(login_url='/signin/')
def deletesection(request, uid, tid, sid):
    gid = GroupTopic.objects.get(tid = tid).group_id
    res_list = TopicResource.objects.filter(user_id = uid, group_id = gid).values_list('rtype', 'rvalue')
    for rtype, rvalue in res_list:
        if rtype not in ('weblink', 'ytlink'):
            remove(settings.MEDIA_ROOT + '/' + str(uid) + '/workspace/' + rvalue)
    TopicSection.objects.get(sid = sid, user_id = uid, group_id = gid, topic_id = tid).delete()
    return redirect('/dashboard/' + str(uid) + '/topic/' + str(tid) + '/')

@login_required(login_url='/signin/')
def add_weblink(request, uid, tid):
    if request.method == "POST":
        name = request.POST['name']
        sid = request.POST['sid']
        url = request.POST['url']
        gid = GroupTopic.objects.get(tid = tid).group_id
        TopicResource.objects.create(
            rname = name,
            rvalue = url,
            rtype = 'weblink',
            section_id = sid,
            group_id = gid,
            topic_id = tid,
            user_id = uid
        ).save()
    return redirect('/dashboard/' + str(uid) + '/topic/' + str(tid) + '/')

@login_required(login_url='/signin/')
def add_ytlink(request, uid, tid):
    if request.method == "POST":
        name = request.POST['name']
        sid = request.POST['sid']
        url = request.POST['url']
        ytlink = get_ytvdo_id(url)
        gid = GroupTopic.objects.get(tid = tid).group_id
        TopicResource.objects.create(
            rname = name,
            rvalue = ytlink,
            rtype = 'ytlink',
            section_id = sid,
            group_id = gid,
            topic_id = tid,
            user_id = uid
        ).save()
    return redirect('/dashboard/' + str(uid) + '/topic/' + str(tid) + '/')

@login_required(login_url='/signin/')
def deletelink(request, uid, tid, rid):
    TopicResource.objects.get(rid = rid, user_id = uid, topic_id = tid).delete()
    return redirect('/dashboard/' + str(uid) + '/topic/' + str(tid) + '/')

@login_required(login_url='/signin/')
def editweblink(request, uid, tid, sid, rid):
    if request.method == "POST":
        name = request.POST['name'] 
        url = request.POST['url']
        ssid = request.POST['sid']
        res = TopicResource.objects.get(user_id = uid, topic_id = tid, section_id = sid, rid = rid)
        res.rname = name
        res.section_id = ssid
        res.rvalue = url
        res.save()
    return redirect('/dashboard/' + str(uid) + '/topic/' + str(tid) + '/')

@login_required(login_url='/signin/')
def editytlink(request, uid, tid, sid, rid):
    if request.method == "POST":
        name = request.POST['name'] 
        url = request.POST['url']
        ssid = request.POST['sid']
        res = TopicResource.objects.get(user_id = uid, topic_id = tid, section_id = sid, rid = rid)
        res.rname = name
        res.section_id = ssid
        res.rvalue = get_ytvdo_id(url)
        res.save()
    return redirect('/dashboard/' + str(uid) + '/topic/' + str(tid) + '/')

@login_required(login_url='/signin/')
def addfile(request, uid, tid, filetype):
    if request.method == 'POST':
        name = request.POST['name']
        sid = request.POST['sid']
        filepath = request.FILES['filepath']
        gid = GroupTopic.objects.get(tid = tid).group_id
        TopicResource.objects.create(
            rname = name,
            rvalue = filepath,
            rtype = filetype,
            section_id = sid,
            group_id = gid,
            topic_id = tid,
            user_id = uid
        ).save()
        tsob = TopicResource.objects.get(rname = name)
        rid = tsob.rid
        modified_filepath = str(uid) + str(gid) + str(tid) + str(rid) + '.' + str(filepath).rsplit('.', 1)[1]
        filepath = str(filepath).replace(' ', '_')
        rename(settings.MEDIA_ROOT + '/' + filepath, settings.MEDIA_ROOT + '/' + modified_filepath)
        tsob.rvalue = modified_filepath
        tsob.save()
        move(settings.MEDIA_ROOT + '/' + modified_filepath, settings.MEDIA_ROOT + '/' + str(uid) + '/workspace')
    return redirect('/dashboard/' + str(uid) + '/topic/' + str(tid) + '/')

@login_required(login_url='/signin/')
def deletefile(request, uid, tid, rid):
    filepath = TopicResource.objects.filter(rid = rid, user_id = uid, topic_id = tid).values_list('rvalue')
    filepath = filepath[0][0]
    remove(settings.MEDIA_ROOT + '/' + str(uid) + '/workspace/' + filepath)
    TopicResource.objects.get(rid = rid, user_id = uid, topic_id = tid).delete()
    return redirect('/dashboard/' + str(uid) + '/topic/' + str(tid) + '/')

@login_required(login_url='/signin/')
def editfile(request, uid, tid, rid):
    if request.method == 'POST':
        rname = request.POST['name']
        sid = request.POST['sid']
        TopicResource.objects.filter(user_id = uid, topic_id = tid, rid = rid).update(rname = rname, section_id = sid)
    return redirect('/dashboard/' + str(uid) + '/topic/' + str(tid) + '/')

@login_required(login_url='/signin/')
def view(request, uid, tid, rid):
    resource_list = TopicResource.objects.filter(topic_id = tid, rid = rid).values_list('rname', 'rvalue', 'rtype')
    res = resource_list[0]
    return render(request, 'view.html', {'rtype' : res[2], 'rname' : res[0], 'rvalue' : res[1]})

def search_videos(request, uid, tid):
    query = request.POST.get('search')
    page_token = request.POST.get('page_token')
    results, next_page_token, prev_page_token  = youtube_search(query, page_token=page_token)
    search_results = {
        'results': results,
        'next_page_token': next_page_token,
        'prev_page_token': prev_page_token,
        'query': query
    }
    return topic(request, uid, tid, search_results)

@login_required(login_url='/signin/')
def groupbytype(request, uid, tid):
    TopicResource.objects.filter(user_id = uid, topic_id = tid, rtype='doc').update(gname = "Documents")
    TopicResource.objects.filter(user_id = uid, topic_id = tid, rtype='ppt').update(gname = "Presentation Files")
    TopicResource.objects.filter(user_id = uid, topic_id = tid, rtype='pdf').update(gname = "PDF Files")
    TopicResource.objects.filter(user_id = uid, topic_id = tid, rtype='img').update(gname = "Images")
    TopicResource.objects.filter(user_id = uid, topic_id = tid, rtype='weblink').update(gname = "Web Links")
    TopicResource.objects.filter(user_id = uid, topic_id = tid, rtype='ytlink').update(gname = "Youtube Links")
    return redirect('/dashboard/' + str(uid) + '/topic/' + str(tid) + '/')