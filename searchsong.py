import requests

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

def extract_songs(data):
    results = []

    sections = data.get("contents", {}) \
                   .get("tabbedSearchResultsRenderer", {}) \
                   .get("tabs", [])[0] \
                   .get("tabRenderer", {}) \
                   .get("content", {}) \
                   .get("sectionListRenderer", {}) \
                   .get("contents", [])

    for section in sections:
        items = section.get("musicShelfRenderer", {}).get("contents", [])
        
        for item in items:
            renderer = item.get("musicResponsiveListItemRenderer")
            if not renderer:
                continue

            title_runs = renderer.get("flexColumns", [])[0] \
                                 .get("musicResponsiveListItemFlexColumnRenderer", {}) \
                                 .get("text", {}) \
                                 .get("runs", [])
            title = title_runs[0]["text"] if title_runs else "Unknown"

            video_id = renderer.get("playlistItemData", {}).get("videoId")

            if video_id:
                results.append({
                    "title": title,
                    "videoId": video_id
                })

    return results

