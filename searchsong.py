import requests
import json

def search_youtube_music(query):
    url = "https://music.youtube.com/youtubei/v1/search?prettyPrint=false"

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Origin": "https://music.youtube.com",
        "Referer": "https://music.youtube.com/"
    }

    payload = {
        "context": {
            "client": {
                "clientName": "WEB_REMIX",
                "clientVersion": "1.20240101.01.00"
            }
        },
        "query": query,
        "params": "EgWKAQIIAWoSEAMQBBAJEAoQBRAREBAQFQ=="
    }

    res = requests.post(url, headers=headers, json=payload)
    data = res.json()

    return data

def extract_video_id(query_data):
    video_id = query_data["contents"]["tabbedSearchResultsRenderer"]["tabs"][0]["tabRenderer"]["content"]["sectionListRenderer"]["contents"][0]["musicCardShelfRenderer"]["title"]['runs'][0]["navigationEndpoint"]["watchEndpoint"]["videoId"]

    return video_id

def get_id(query):
    data = search_youtube_music(query)
    return extract_video_id(data)




