from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler

TOKEN = '7893622203:AAGEu1OQ1TjuRegqFprAtKTQLSeuJb0hY0Q'
OWNER_ID = 7728185213

app = Flask(__name__)
bot = Bot(token=TOKEN)

dispatcher = Dispatcher(bot=bot, update_queue=None, use_context=True)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="🤖 বট কাজ করছে!")

dispatcher.add_handler(CommandHandler("start", start))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'OK'

@app.route('/')
def index():
    return '✅ Bot is running.'

if __name__ == '__main__':
    app.run()
