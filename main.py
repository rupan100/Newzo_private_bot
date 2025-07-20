from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler

TOKEN = "7598919656:AAEpAwoqrzjizDmJS75vJsoOLv3rFf_2HZ0"
bot = Bot(token=TOKEN)
app = Flask(__name__)

# Start command handler
def start(update: Update, context):
    update.message.reply_text("👋 হ্যালো! আমি প্রস্তুত আছি!")

# Dispatcher setup
dispatcher = Dispatcher(bot, None, workers=0, use_context=True)
dispatcher.add_handler(CommandHandler("start", start))

@app.route('/')
def index():
    return "✅ Bot is running on Render!"

@app.route(f"/{TOKEN}", methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

if __name__ == "__main__":
    app.run(port=10000)
