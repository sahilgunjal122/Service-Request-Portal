import requests
from .models import TelegramUser
from decouple import config

TOKEN = config('TELEGRAM_BOT_TOKEN')
URL = f'https://api.telegram.org/bot{TOKEN}/'

def get_updates():
    response = requests.get(URL + 'getUpdates')
    return response.json()

def save_new_users():
    data = get_updates()
    for item in data.get('result', []):
        msg = item.get('message')
        if msg and msg.get('text') == '/start':
            user = msg['from']
            tg_id = user['id']
            username = user.get('username') or f"{user['first_name']}_{tg_id}"

            TelegramUser.objects.get_or_create(
                telegram_id=tg_id,
                defaults={'telegram_username': username}
            )
