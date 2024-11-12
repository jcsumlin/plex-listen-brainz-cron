import os
from dotenv import load_dotenv
import pylistenbrainz
import logging

load_dotenv()

TOKEN = os.getenv('LISTENBRAINZ_TOKEN')
DEBUG = bool(os.getenv('DEBUG'))

if not TOKEN:
    raise ValueError('LISTENBRAINZ_TOKEN must be set in the environment')

client = pylistenbrainz.ListenBrainz()
client.set_auth_token(TOKEN)

logger = logging.getLogger(__name__)

def create_listen(track: dict):
    """
    Create a new Listen object and submit it to ListenBrainz
    """
    new_listen = pylistenbrainz.Listen(
        track_name=track['title'],
        artist_name=track['grandparent_title'],
        listened_at=track['date'],
        listening_from='PlexAmp'
    )
    if DEBUG:
        logging.debug("Would have submitted Listen for {}".format(track['full_title']))
        return None
    logger.debug("Recording new Listen for {}".format(track['full_title']))
    return client.submit_single_listen(new_listen)