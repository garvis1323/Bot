from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# توکن ربات
TOKEN = "7509826144:AAE5A5dWTWcwbKWmtuYXvTGKC0PXTr5SWVo"

# لیست سوالات و جواب‌های برعکس
reverse_responses = {
    "سلام": "خداحافظ",
    "خداحافظ": "سلام",
    "خوبی؟": "بد نیستم",
    "حالت چطوره؟": "حالم بده",
    "صبح بخیر": "شب بخیر",
    "شب بخیر": "صبح بخیر",
    "چطوری؟": "بدک نیستم",
    "مرسی": "خواهش نمی‌کنم",
    "بای": "سلام",
    "هی": "برو",
    "دوستت دارم": "من دوستت ندارم",
    "چه خبر؟": "هیچی",
    "کجایی؟": "نمی‌دونم",
    "بیکارم": "سرت رو گرم کن"
}

# تابع /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! هرچی بگی برعکسشو می‌گم 😄")

# تابع جواب‌دهی به پیام‌ها
async def reverse_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.strip()
    response = reverse_responses.get(user_message, "نمی‌فهمم چی می‌گی 🤔")
    await update.message.reply_text(response)

# ساخت ربات
app = ApplicationBuilder().token(TOKEN).build()

# اضافه کردن دستورات و پیام‌ها
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reverse_reply))

# اجرای ربات
print("✅ ربات معکوس روشن شد!")
app.run_polling()
