import os
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", 8080))
APP_URL = os.getenv("APP_URL")  # es: https://italianfarm.up.railway.app

LOGO_URL = "https://tgwos.github.io/ITALIANFARM/5807439531530194108.jpg"
CATALOG_URL = "https://tgwos.github.io/ITALIANFARM/"

def main_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📦 Apri Catalogo", web_app=WebAppInfo(url=CATALOG_URL))],
        [InlineKeyboardButton("📞 Contatti ufficiali", callback_data="contacts")],
    ])

def back_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⬅️ Indietro", callback_data="back")]
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo=LOGO_URL,
        caption="🌱 BENVENUTI SU ITALIAN FARM BOT 🌱",
        reply_markup=main_keyboard()
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "contacts":
        await query.edit_message_caption(
            caption="📱 CONTATTI UFFICIALI\n\n@Italianfarm1",
            reply_markup=back_keyboard()
        )

    elif query.data == "back":
        await query.edit_message_caption(
            caption="🌱 BENVENUTI SU ITALIAN FARM BOT 🌱",
            reply_markup=main_keyboard()
        )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"{APP_URL}/{TOKEN}"
    )

if __name__ == "__main__":
    main()
