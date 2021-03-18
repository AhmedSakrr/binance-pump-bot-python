from telethon import TelegramClient, events, sync

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 3045614
api_hash = '04e617781f226929eb72b8915654a5e7'

client = TelegramClient('session_read', api_id, api_hash)

@client.on(events.NewMessage(chats=("GroupName", "Telegram")))
async def my_event_handler(event):
    message = event.text
    divider = message.index('#')
    coin = message[divider + 1 : divider + 4]
    print(coin)

client.start()
client.run_until_disconnected()