from telegram.ext import Updater, CommandHandler
import random

# Replace with your token
TOKEN = "8269558382:AAF3FJzN0k8laZmj4P27mI1YSQfN6ZYjH9g"

# Sample vocab list (we can expand later or pull from a file/API)
VOCAB = [
    {"word": "Eloquent", "meaning": "Fluent or persuasive in speaking or writing", "example": "She gave an eloquent speech that moved everyone."},
    {"word": "Pragmatic", "meaning": "Dealing with things practically and realistically", "example": "He took a pragmatic approach to solving the problem."},
    {"word": "Resilient", "meaning": "Able to recover quickly from difficulties", "example": "Children are often more resilient than adults expect."},
    {"word": "Serendipity", "meaning": "The occurrence of events by chance in a happy way", "example": "Meeting her at the café was pure serendipity."},
]

def start(update, context):
    update.message.reply_text("Hey baddie 🌸! I’m alive and ready to help you level up 🚀")

def vocab(update, context):
    word = random.choice(VOCAB)
    message = f"✨ *Word:* {word['word']}\n📖 *Meaning:* {word['meaning']}\n💡 *Example:* {word['example']}"
    update.message.reply_text(message, parse_mode="Markdown")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("vocab", vocab))  # new command

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
