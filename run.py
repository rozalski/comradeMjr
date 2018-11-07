#!./env/bin/python3.5
from telethon import TelegramClient, sync, events # для получения сообщений
import sys, re
# https://my.telegram.org/auth?to=apps регистрация приложения телеграм
# https://telegram.org/support писать на разбан
api_id = 508152
api_hash = '3ad19da000be0e616ead7455be03b42b'
phone = '+79154103557'

client = TelegramClient('current-session', api_id, api_hash)
print('Подключение...')
@client.on(events.NewMessage(incoming=True, outgoing=True))
async def normal_handler(event):
    if event.document:
        if(event.document.to_dict()['mime_type'] == 'application/vnd.android.package-archive'):
            await event.delete()
    date = event.message.to_dict()['date']
    message = event.message.to_dict()['message']
    if(bool(re.search('[\u0627-\u064a]', message))):
        result = 'Содержит арабский'
        await event.delete()
    else:
        result = 'Нет арабского'
    print('[{}] {} : {}'.format(date, message, result))
client.start()
if not client.is_user_authorized():
    try:
        #client.send_code_request(phone) #при первом запуске - раскомментить,
        #после авторизации для избежания FloodWait советую закомментить
        print('Sending a code...')
        client.sign_in(phone, input('Enter code: '))
        print('Successfully!')
    except FloodWaitError as FloodError:
        print('Flood wait: {}.'.format(FloodError))
        sys.exit()
    except SessionPasswordNeededError:
        client.sign_in(password=getpass('Enter password: '))
print('Подключено!')

#Получаем всех пользователей
# participants = client.get_participants(chat2)
# users={}
#
# for partic in client.iter_participants(chat2):
#     lastname=""
#     if partic.last_name:
#        lastname=partic.last_name
#     users[partic.id]=partic.first_name+" "+lastname

client.run_until_disconnected()
client.disconnect()
print('Подключение закрыто.')
sys.exit()
