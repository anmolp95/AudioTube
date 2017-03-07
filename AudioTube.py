import requests
import json
API_KEY="AIzaSyDR4qtKowtX9gAbDMrg4C5suHKRe2L3fj4"
query="\"zalima\""
typ="video"
req="https://www.googleapis.com/youtube/v3/search?"
req=req+"key="+API_KEY+"&part=snippet&maxResults=5&type="+typ+"&q="+query
gt=requests.get(req)
x=json.loads(gt.text)
for item in x["items"]:
    print item["snippet"]["title"],item["id"]["videoId"]
    
    
