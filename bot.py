from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token="5673240432:AAEQFzBJWqOyihuzll8K1OGqLemKW7kf9y8", use_context=True)

scoreboard = {} 

def shame_blasphemers(update, context):
    #substring condition
    message = update.message
    curse_list = ["fk", "fuck", "shit", "shat", "bitch", "mf", "kos omak", "asshole", "cock", "dick", "pussy", "clit", "cunt", "dyke", "kike", "nigga", "piss", "slut", "whore", "twat", "wank", "prick", "nigger", "arsehole", "chink"]
    curse_score = sum([message.text.lower().count(curse.lower()) if curse.lower() in message.text.lower() else 0 for curse in curse_list])

    if curse_score>0:
        #identify who blashpemed and punish appropriately
        user = message.from_user
        user_name = user.first_name

        if user_name in scoreboard:
            scoreboard[user_name]+=curse_score
        else:
            scoreboard[user_name]=curse_score

        sorted_scoreboard = sorted(scoreboard, key=scoreboard.get, reverse=True)
        results = "\n".join([(user_name+": "+str(sorted_scoreboard[user_name])) for user_name in sorted_scoreboard])
        message.reply_text("Blasphemy Tally:\n"+results)


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

