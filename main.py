import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TELEGRAM_TOKEN = 'YOUR_TELEGRAM_TOKEN'
OLLAMA_URL = 'http://localhost:11434/api/chat'

MODEL = 'OLLAMA_MODEL'

SYSTEM_PROMPT = ""

async def chat_with_ollama(message):
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message}
        ],
        "stream": False
    })

    data = response.json()
    return data.get("message", {}).get("content", "can't answer for now")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    reply = await chat_with_ollama(user_message)
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("BOT is active... 🚀")
app.run_polling()