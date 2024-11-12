import os
from dotenv import load_dotenv

from gotify_api import gotify
from listen_brainz import listen_brainz
from tautulli_api import get_history
import logging
load_dotenv()

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(name)s:%(message)s")
logger = logging.getLogger(__name__)


DEBUG = bool(os.getenv('DEBUG'))

if __name__ == '__main__':
    logger.debug('Starting ListenBrainz submission process')
    if DEBUG:
        logger.debug('Debug mode enabled')
    history = get_history.get_history()
    if len(history) == 0:
        logger.debug('No new listens, exiting...')
        exit()
    logger.debug('{} new listens found, submitting to ListenBrainz'.format(len(history)))
    for track in history:
        listen_brainz.create_listen(track)

    gotify.send_log('ListenBrainz submission', 'Submitted {} listens to ListenBrainz\n{}'.format(len(history), '\n - '.join([track['full_title'] for track in history])))
    if DEBUG:
        logger.debug('New last track date: {}'.format(history[0]['date']))
        logger.debug('Debug mode enabled, exiting')
        exit()
    get_history.write_last_track_date(str(history[0]['date']))


# recs = client.get_user_recommendation_recordings('liquidWiFi')
