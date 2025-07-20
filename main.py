from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
import os

TOKEN = os.environ.get('BOT_TOKEN')  # Render এ Environment Variable হিসেবে সেট করুন
bot = Bot(token=TOKEN)

app = Flask(__name__)

def start(update, context):
    update.message.reply_text("হ্যালো! আমি চালু আছি ✅")

dispatcher = Dispatcher(bot=bot, update_queue=None, use_context=True)
dispatcher.add_handler(CommandHandler("start", start))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK"

@app.route("/", methods=["GET"])
def home():
    return "Bot is running!"

if __name__ == "__main__":
    app.run(port=10000)
