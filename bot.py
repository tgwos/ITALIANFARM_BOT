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

# 🔐 TOKEN
TOKEN = os.getenv("BOT_TOKEN")
# TOKEN = "INSERISCI_QUI_IL_TOKEN"

# 🌐 URL
LOGO_URL = "https://tgwos.github.io/ITALIANFARM/5807439531530194108.jpg"
CATALOG_URL = "https://tgwos.github.io/ITALIANFARM/"

TELEGRAM_CONTACT_URL = "https://t.me/italianfarm11"
TELEGRAM_GROUP_URL = "https://t.me/+TJZTE4SGZBRhNTE0"
SIGNAL_URL = "https://signal.me/#eu/kRf_X-QX9q6AnKI0IC9lsi2GjAiS7cLKf_MoHkGnHt1U3msPbTJOYJ7C2IOfVkU5"
INSTAGRAM_URL = "https://www.instagram.com/la_fattoria____/"

# 🏠 Menu principale premium
def main_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🛒 Apri Catalogo", web_app=WebAppInfo(url=CATALOG_URL))],
        [InlineKeyboardButton("📞 Contatti Ufficiali", callback_data="contacts")],
        [InlineKeyboardButton("👥 Canale Telegram", url=TELEGRAM_GROUP_URL)],
    ])

# 📞 Menu contatti premium
def contacts_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("✈️ Telegram", url=TELEGRAM_CONTACT_URL)],
        [InlineKeyboardButton("📶 Signal", url=SIGNAL_URL)],
        [InlineKeyboardButton("📷 Instagram", url=INSTAGRAM_URL)],
        [InlineKeyboardButton("⬅️ Indietro", callback_data="back")]
    ])

# 🚀 /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo=LOGO_URL,
        caption=(
            "🏪 ITALIAN FARM — OFFICIAL BOT\n"
            "━━━━━━━━━━━━━━\n\n"
            "Benvenuto nel menu ufficiale.\n"
            "Scegli una sezione qui sotto:\n\n"
            "🛒 Catalogo\n"
            "Consulta prodotti, info e disponibilità.\n\n"
            "📞 Contatti ufficiali\n"
            "Telegram, Signal e Instagram.\n\n"
            "👥 Community Telegram\n"
            "Accedi al canale ufficiale.\n\n"
            "━━━━━━━━━━━━━━\n"
            "✅ Supporto rapido\n"
            "🔒 Solo canali ufficiali\n"
            "📦 Catalogo sempre aggiornato"
        ),
        reply_markup=main_keyboard()
    )

# 🔘 Gestione pulsanti
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "contacts":
        await query.edit_message_caption(
            caption=(
                "📞 CONTATTI UFFICIALI\n"
                "━━━━━━━━━━━━━━\n\n"
                "Scegli dove contattarci:\n\n"
                "✈️ Telegram\n"
                "Supporto diretto.\n\n"
                "📶 Signal\n"
                "Canale privato di contatto.\n\n"
                "📷 Instagram\n"
                "Profilo ufficiale.\n\n"
                "━━━━━━━━━━━━━━"
            ),
            reply_markup=contacts_keyboard()
        )

    elif query.data == "back":
        await query.edit_message_caption(
            caption=(
                "🏪 ITALIAN FARM — OFFICIAL BOT\n"
                "━━━━━━━━━━━━━━\n\n"
                "Benvenuto nel menu ufficiale.\n"
                "Scegli una sezione qui sotto:\n\n"
                "🛒 Catalogo\n"
                "Consulta prodotti, info e disponibilità.\n\n"
                "📞 Contatti ufficiali\n"
                "Telegram, Signal e Instagram.\n\n"
                "👥 Community Telegram\n"
                "Accedi al canale ufficiale.\n\n"
                "━━━━━━━━━━━━━━\n"
                "✅ Supporto rapido\n"
                "🔒 Solo canali ufficiali\n"
                "📦 Catalogo sempre aggiornato"
            ),
            reply_markup=main_keyboard()
        )

# ▶️ Avvio bot
def main():
    if not TOKEN:
        raise RuntimeError("❌ BOT_TOKEN non impostato")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    print("✅ Bot premium avviato correttamente")
    app.run_polling()

if __name__ == "__main__":
    main()

