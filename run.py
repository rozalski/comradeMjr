#!./env/bin/python3.5
from telethon import TelegramClient, sync, events
import sys
api_id = 508152
api_hash = '3ad19da000be0e616ead7455be03b42b'
chat = 'https://t.me/joinchat/LWuqAlgRV3mDiuH3uYyB_Q'
client = TelegramClient('current-session', api_id, api_hash)
print('Подключение...')
@client.on(events.NewMessage(chats=(chat)))
async def normal_handler(event):
    date = event.message.to_dict()['date']
    user = users[event.message.to_dict()['from_id']]
    message = event.message.to_dict()['message']
    print('[{}] {} : {}'.format(date, user, message))
    #print(f"{date}: {user} : {message}")
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
participants = client.get_participants(chat)
users={}

for partic in client.iter_participants(chat):
    lastname=""
    if partic.last_name:
       lastname=partic.last_name
    users[partic.id]=partic.first_name+" "+lastname
print(users)

#messages = client.get_entity(chat)
#messages = client.get_messages(chat)
#mes = client.get_participants(chat)
#print(messages)
#print(mes)
client.run_until_disconnected()
client.disconnect()
print('Подключение закрыто.')
sys.exit()
