from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler

TOKEN = "7893622203:AAGEu1OQ1TjuRegqFprAtKTQLSeuJb0hY0Q"
OWNER_ID = 7728185213

bot = Bot(token=TOKEN)
app = Flask(__name__)

dispatcher = Dispatcher(bot=bot, update_queue=None, workers=0, use_context=True)

def start(update, context):
    if update.effective_user.id == OWNER_ID:
        update.message.reply_text("✅ Bot is Working!")

dispatcher.add_handler(CommandHandler("start", start))

@app.route("/", methods=["POST", "GET"])
def webhook():
    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
    return "Working!", 200

if __name__ == '__main__':
    app.run()
