from telethon import TelegramClient, sync, events
import sys, re
# from langdetect import detect
api_id = 508152
api_hash = '3ad19da000be0e616ead7455be03b42b'
#chat = '-1001389028016'
# chat = {'https://t.me/joinchat/LWuqAlgRV3mDiuH3uYyB_Q', 'https://t.me/joinchat/LWuqAhKU-7wKy_P_e1sNTA'}
#боевые чаты
# ch1 = 'https://t.me/joinchat/GbTZxEEbux6nbboyWcpNpw'
# ch2 = 'https://t.me/joinchat/EJzxUkDP6NZLhToKVpGYOQ'
# ch3 = 'https://t.me/joinchat/EJzxUkGKFxM5gGn2ZA0IyA'
# ch4 = 'https://t.me/joinchat/EJzxUkBmFMY8qvPmKowdoA'
# ch5 = 'https://t.me/joinchat/EJzxUkCaG2GDbTMD7DgL9A'
# ch6 = 'https://t.me/joinchat/EJzxUj_dAsuSNNTHWiahKw'
# ch7 = 'https://t.me/joinchat/EJzxUkFUDYVxF0XFppKxrg'
# ch8 = 'https://t.me/joinchat/EJzxUkDLiQGHiq6_dpAX0A'
# ch9 = 'https://t.me/joinchat/EJzxUkFLN3JMbcg6QPDdQw'
# ch10 = 'https://t.me/joinchat/EJzxUkDaPrvLISdLG8aLiQ'
# ch11 = 'https://t.me/joinchat/EJzxUj8Fw79nQc_9-VTqEg'
# ch12 = 'https://t.me/joinchat/EJzxUkCaG2GDbTMD7DgL9A'
# ch13 = 'https://t.me/joinchat/EJzxUkYIUou4TZW-bRV3eQ'
# ch14 = 'https://t.me/joinchat/EJzxUkmOTNP8aMrO6C6RsQ'
# ch15 = 'https://t.me/joinchat/EJzxUkrRtQnMxWH85woxOg'
# ch16 = 'https://t.me/joinchat/EJzxUkVuVjqi5zrFoRgIeQ'
# ch17 = 'https://t.me/joinchat/EJzxUkkck2jJFVGuwHP2Ng'
# ch18 = 'https://t.me/joinchat/EJzxUlDD_rDK_bKH0k0cGw'
# ch19 = 'https://t.me/joinchat/EJzxUkwnP9L5wRFT3erwHA'
# ch20 = 'https://t.me/joinchat/EJzxUkp9n8CdF072aoRUrg'
# ch21 = 'https://t.me/joinchat/EJzxUkZ2YWmjmght1f7aXw'
# ch22 = 'https://t.me/joinchat/EJzxUkiF6e56i009zoRXhQ'
# ch23 = 'https://t.me/joinchat/EJzxUk5SSFYxu4_KBlFBIQ'
# ch24 = 'https://t.me/joinchat/EJzxUlIS4seALI4tlGY2bQ'
# ch25 = 'https://t.me/joinchat/EJzxUkaUaN34zcjiiPBfXQ'
# ch26 = 'https://t.me/joinchat/EJzxUk_ZZjp4SinHw3-rwQ'
#тестовые чаты
chat = 'https://t.me/joinchat/LWuqAlgRV3mDiuH3uYyB_Q'
chat2 = 'https://t.me/joinchat/LWuqAhKU-7wKy_P_e1sNTA'

client = TelegramClient('current-session', api_id, api_hash)
print('Подключение...')
@client.on(events.NewMessage(chats=(chat, chat2)))#chats=(chat, chat2, ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8,
#ch9, ch10, ch11, ch12, ch13, ch14, ch15, ch16, ch17, ch18, ch19, ch20, ch21, ch22, ch23,
#ch24, ch25, ch26)))
async def normal_handler(event):
    date = event.message.to_dict()['date']
    user = users[event.message.to_dict()['from_id']]
    message = event.message.to_dict()['message']
    result = bool(re.search('[\u0627-\u064a]', message))
    print('[{}] {} : {} | {}'.format(date, user, message, result))
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
#print(users)

#messages = client.get_entity(chat)
#messages = client.get_messages(chat)
#mes = client.get_participants(chat)
#print(messages)
#print(mes)
client.run_until_disconnected()
client.disconnect()
print('Подключение закрыто.')
sys.exit()
