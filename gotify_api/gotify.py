import os
from dotenv import load_dotenv
from gotify import Gotify

load_dotenv()

GOTIFY_URL = os.getenv('GOTIFY_URL')
GOTIFY_APP_TOKEN = os.getenv('GOTIFY_APP_TOKEN')
if not GOTIFY_URL or not GOTIFY_APP_TOKEN:
    raise ValueError('GOTIFY_URL and GOTIFY_APP_TOKEN must be set in the environment')

gotify = Gotify(
    base_url=GOTIFY_URL,
    app_token=GOTIFY_APP_TOKEN,
)

def send_log(title, message):
    gotify.create_message(
        message,
        title=title,
        priority=0,
    )