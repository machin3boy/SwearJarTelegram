#pip install python-telegram-bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token="BOT_TOKEN", use_context=True)
groups = updater.bot.get_my_groups()

scoreboard = {} 

for group in groups:

    if group.username == "GROUP_ID"
        
        for message in group.history():

            #substring condition
            curse_list = ["curse1", "curse2"]
            curse_score = sum([1 if curse.lower() in message.text.lower() else 0 for curse in curse_list)]

            if curse_score>0:
                #identify who blashpemed and punish appropriately
                user = message.from_user
                user_name = user.first_name

                if user_name in scoreboard:
                    scoreboard[user_name]+=curse_score
                else:
                    scoreboard[user_name]=curse_score

                sorted_scoreboard = sorted(scoreboard, key=scoreboard.get, reverse=True)
                results = "\n".join([user_name+": "+scoreboard[user_name] for user_name in scoreboard])
                group.send_message("Someone has blasphemed...\n\nNew scoreboard:\n"+results)

