#pip install python-telegram-bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token="BOT_TOKEN", use_context=True)
groups = updater.bot.get_my_groups()
for group in groups:
    messages = group.history()

    for message in messages:
    if "swear word substring" in message.text: #to add conditions
        #identify who blashpemed and punish appropriately here
        group.send_message("The substring was found in this message: " + message.text)
        user = message.from_user
        user_name = user.first_name

