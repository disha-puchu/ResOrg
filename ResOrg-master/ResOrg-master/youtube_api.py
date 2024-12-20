# search/youtube_api.py
from googleapiclient.discovery import build
from django.conf import settings

def youtube_search(query, max_results=5, page_token=None):
    youtube = build(serviceName='youtube', version='v3', developerKey='AIzaSyA5Hgs0_AZpLs8uzPW7dNAi3BAupl01v6U')
    
    search_response = youtube.search().list(
        q=query,
        part = 'snippet',
        maxResults=max_results,
        pageToken=page_token,
    ).execute()
    
    results = []
    for item in search_response.get('items', []):
        video_id = item['id'].get('videoId')
        snippet = item['snippet']
        channel_id = snippet['channelId']
        
        video_details = {
            'title': snippet['title'],
            'description': snippet['description'],
            'publishedAt': snippet['publishedAt'],
            'videoId': video_id,
            'channelTitle': snippet['channelTitle']
        }
        
        # Get video statistics
        if video_id is None:
            video_details['viewCount'] = 'NA'
        else:
            video_response = youtube.videos().list(part = 'id, statistics', id = video_id).execute()
            for video in video_response.get('items', []):
                pass
                video_details['viewCount'] = video['statistics'].get('viewCount', 0)


        # Get channel details to fetch the channel icon
        channel_response = youtube.channels().list(
            part='snippet',
            id=channel_id
        ).execute()
        
        for channel in channel_response.get('items', []):
            video_details['channelIcon'] = channel['snippet']['thumbnails']['default']['url']
        
        results.append(video_details)
    
    next_page_token = search_response.get('nextPageToken')
    prev_page_token = search_response.get('prevPageToken')
    return results, next_page_token, prev_page_token
