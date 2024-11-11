import os
from dotenv import load_dotenv

from tautulli import RawAPI
import pylistenbrainz
import datetime
load_dotenv()


TOKEN = os.getenv('LISTENBRAINZ_TOKEN')
TAUTULLI_API_KEY = os.getenv('TAUTULLI_API_KEY')
TAUTULLI_URL = os.getenv('TAUTULLI_URL')
client = pylistenbrainz.ListenBrainz()
client.set_auth_token(TOKEN)
with open('last_track.txt', 'r') as f:
    last_track_date = f.read()
    try:
        ts = int(last_track_date)
        filter_date = datetime.datetime.fromtimestamp(ts, datetime.UTC)
    except ValueError:
        filter_date = datetime.datetime.now()

def filter_history(history, filter_date):
    tracks = []
    for track in history:
        if datetime.datetime.fromtimestamp(track['date'], datetime.UTC) > filter_date:
            if track['percent_complete'] <= 50:
                print("Skipping {} because it was not played for more than 50% of the track".format(track['full_title']))
                continue
            tracks.append(track)
    return tracks
    

# Create Tautulli client
taut = RawAPI(api_key=TAUTULLI_API_KEY, base_url=TAUTULLI_URL)
history = taut.get_history(user='jcsumlin', media_type='track', after=filter_date)
# Filter out tracks that have already been submitted
# THe after param should have taken care of this but it seems to be broken
filtered_history = filter_history(history['data'], filter_date)

if len(filtered_history) == 0:
    print('No new listens')
    exit()
for track in filtered_history:
    new_listen = pylistenbrainz.Listen(
        track_name=track['title'],
        artist_name=track['grandparent_title'],
        listened_at=track['date'],
        listening_from='PlexAmp'
    )
    print("Recording new Listen for {}".format(track['full_title']))
    client.submit_single_listen(new_listen)
with open('last_track.txt', 'w') as f:
    f.write(str(history['data'][0]["date"]))


# recs = client.get_user_recommendation_recordings('liquidWiFi')
