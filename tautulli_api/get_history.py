import datetime
import logging
from tautulli import RawAPI
import os
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)


TAUTULLI_API_KEY = os.getenv('TAUTULLI_API_KEY')
TAUTULLI_URL = os.getenv('TAUTULLI_URL')
PLEX_USER = os.getenv('PLEX_USER')
if [TAUTULLI_API_KEY, TAUTULLI_URL, PLEX_USER].count(None) > 0:
    raise ValueError('TAUTULLI_API_KEY, TAUTULLI_URL, and PLEX_USER must be set in the environment')

def read_last_track_date():
    with open('last_track.txt', 'r') as f:
        last_track_date = f.read()
        try:
            ts = int(last_track_date)
            filter_date = datetime.datetime.fromtimestamp(ts, datetime.UTC)
        except ValueError:
            filter_date = datetime.datetime.now()
    return filter_date

def write_last_track_date(date: str):
    with open('last_track.txt', 'w') as f:
        f.write(date)
    logger.debug('Wrote last track date to file')

def filter_history(history, filter_date):
    tracks = []
    for track in history:
        if datetime.datetime.fromtimestamp(track['date'], datetime.UTC) > filter_date:
            if track['percent_complete'] <= 50:
                logger.debug("Skipping {} because it was not played for more than 50% of the track".format(track['full_title']))
                continue
            tracks.append(track)
    return tracks

def get_history() -> list[dict]:
    filter_date = read_last_track_date()
    # Create Tautulli client
    taut = RawAPI(api_key=TAUTULLI_API_KEY, base_url=TAUTULLI_URL)
    history = taut.get_history(user=PLEX_USER, media_type='track', after=filter_date)
    # Filter out tracks that have already been submitted
    # THe after param should have taken care of this but it seems to be broken
    filtered_history = filter_history(history['data'], filter_date)
    return filtered_history