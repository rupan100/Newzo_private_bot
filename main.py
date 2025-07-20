from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
import logging

# Bot Token
BOT_TOKEN = "7893622203:AAGEu1OQ1TjuRegqFprAtKTQLSeuJb0hY0Q"
OWNER_ID = 7728185213

# Flask app init
app = Flask(__name__)
bot = Bot(token=BOT_TOKEN)

# Logging setup (for debugging)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Dispatcher setup
dispatcher = Dispatcher(bot, None, workers=0)

# /start command handler
def start(update, context):
    user_id = update.effective_user.id
    if user_id == OWNER_ID:
        context.bot.send_message(chat_id=update.effective_chat.id, text="✅ আপনি এই বটের মালিক!")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="❌ আপনি এই বটের মালিক নন!")

# Register handler
dispatcher.add_handler(CommandHandler("start", start))

# Route for webhook
@app.route('/', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK"

# App run (used by Render)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
