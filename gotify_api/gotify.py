import os
from dotenv import load_dotenv
from gotify import Gotify

load_dotenv()

GOTIFY_URL = os.getenv('GOTIFY_URL')
GOTIFY_APP_TOKEN = os.getenv('GOTIFY_APP_TOKEN')

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