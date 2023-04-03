import requests as rq
from deep_translator import GoogleTranslator
import time, json

translator = GoogleTranslator(source='auto', target='ru')


API_URL : str = 'https://api.telegram.org/bot'
BOT_TOKEN : str = '6093461770:AAHpuUMCblkp5iZVq36sfEDDg3_V5-Vykcc'
TEXT : str
MAX_COUNTER : int = 50

offset : int = -2
counter : int = 0
chat_id : int


while counter < MAX_COUNTER:

    print('atemp:', counter)

    updates = rq.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset+1}').json()

    if updates['result']:
        for result in updates['result']:

            answer_user = result['message']['text']

            api_url_num = 'http://numbersapi.com/' + str(answer_user)

            response = rq.get(api_url_num)
            TEXT = translator.translate(response.text)


            chat_id = result['message']['from']['id']
            offset = result['update_id']

            rq.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')
           
    time.sleep(1)
    counter += 1