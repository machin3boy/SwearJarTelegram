from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token="BOT_API_TOKEN", use_context=True)

scoreboard = {} 

def shame_blasphemers(update, context):
    #substring condition
    message = update.message
    curse_list = ["curse word", "curse word 2, etc."]
    curse_score = sum([message.text.lower().count(curse.lower()) if curse.lower() in message.text.lower() else 0 for curse in curse_list])

    if curse_score>0:
        #identify who blashpemed and punish appropriately
        user = message.from_user
        user_name = user.first_name

        if user_name in scoreboard:
            scoreboard[user_name]+=curse_score
        else:
            scoreboard[user_name]=curse_score

        sorted_scoreboard = sorted(scoreboard.items(), key=scoreboard.get, reverse=True)

        results = "\n".join([score[0]+ ": " + str(score[1]) for score in sorted_scoreboard])
        message.reply_text("Blasphemy Tally (find god):\n\n"+results)


# Get the dispatcher to register handlers.
dispatcher = updater.dispatcher

# Add a command handler all group messages.
blasphemy_handler = MessageHandler(Filters.text, shame_blasphemers)
dispatcher.add_handler(blasphemy_handler)

# Start the Bot.
updater.start_polling()

# Run the bot until you press Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT. This should be used most of the time, since
# start_polling() is non-blocking and will stop the bot gracefully.
updater.idle()

