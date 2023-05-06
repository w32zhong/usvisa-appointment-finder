import requests
from creds import telegram_bot_token, telegram_chat_id


def send_message(text):
    url = f'https://api.telegram.org/bot{telegram_bot_token}/sendMessage'
    parameters = {
        'chat_id': telegram_chat_id,
        'text': text
    }
    return requests.post(url, parameters)


def send_photo(photo_file):
    url = f'https://api.telegram.org/bot{telegram_bot_token}/sendPhoto'
    parameters = {
        'chat_id': telegram_chat_id
    }
    return requests.post(url, parameters, files={'photo': photo_file})

def get_me():
    url = f'https://api.telegram.org/bot{telegram_bot_token}/getMe'
    return requests.get(url).text

def get_update():
    url = f'https://api.telegram.org/bot{telegram_bot_token}/getUpdates'
    return requests.get(url).text
