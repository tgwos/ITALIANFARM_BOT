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

TELEGRAM_GROUP_URL = "https://t.me/+TIzcbA_vAMw4ZjU0"
SIGNAL_GROUP_URL = "https://signal.group/#CjQKIDNGRGl9UmFJzST3ADxn0PsPIc0zsRWW1foOy3Ity-KvEhBjRjUNbHUuV1qczApKp_ok"

# 🔹 Tastiera principale
def main_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📦 Apri Catalogo", web_app=WebAppInfo(url=CATALOG_URL))],
        [InlineKeyboardButton("📞 Contatti ufficiali", callback_data="contacts")],
        [InlineKeyboardButton("💳 Metodo di pagamento", callback_data="payment")],
        [InlineKeyboardButton("👥 Canale Telegram", url=TELEGRAM_GROUP_URL)],
        [InlineKeyboardButton("🔐 Gruppo Signal", url=SIGNAL_GROUP_URL)],
    ])

# 🔹 Tastiera indietro
def back_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⬅️ Indietro", callback_data="back")]
    ])

# 🔹 /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo=LOGO_URL,
        caption="👑 *BENVENUTO SU ITALIAN FARM BOT* 👑\n\nSeleziona un'opzione dal menu qui sotto:",
        parse_mode="Markdown",
        reply_markup=main_keyboard()
    )

# 🔹 Gestione pulsanti
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "contacts":
        await query.edit_message_caption(
            caption=(
                "📱 *CONTATTI UFFICIALI*\n\n"
                "✈️ *Telegram*\n"
                "@Italianfarm1\n\n"
                "📶 *Signal*\n"
                "https://signal.me/#eu/kRf_X-QX9q6AnKI0IC9lsi2GjAiS7cLKf_MoHkGnHt1U3msPbTJOYJ7C2IOfVkU5\n\n"
                "🥔 *Potato*\n"
                "https://tutuduanyu.org/italianfarm"
            ),
            parse_mode="Markdown",
            reply_markup=back_keyboard()
        )

    elif query.data == "payment":
        await query.edit_message_caption(
            caption=(
                "💳 *METODI DI PAGAMENTO*\n\n"
                "🚚 *Delivery / Meetup*\n"
                "Pagamento in contanti alla consegna.\n\n"
                "📦 *Spedizione (Ship)*\n"
                "Pagamento anticipato tramite:\n"
                "• 🪙 Criptovalute\n"
                "• 💳 Ricarica Postepay presso tabaccheria\n\n"
                "🤝 *Escrow accettato*\n\n"
               
            ),
            parse_mode="Markdown",
            reply_markup=back_keyboard()
        )

    elif query.data == "back":
        await query.edit_message_caption(
            caption="🌱 *BENVENUTO SU ITALIAN FARM BOT* 🌱\n\nSeleziona un'opzione dal menu:",
            parse_mode="Markdown",
            reply_markup=main_keyboard()
        )

# 🔹 Avvio bot
def main():
    if not TOKEN:
        raise RuntimeError("❌ BOT_TOKEN non impostato")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    print("✅ Bot avviato correttamente")
    app.run_polling()

# ✅ ENTRY POINT CORRETTO
if __name__ == "__main__":
    main()
