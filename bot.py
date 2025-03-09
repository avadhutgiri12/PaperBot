from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, CallbackContext

# Dictionary with question paper links
question_papers = {
    "Class 10 - Mathematics": "https://www.dropbox.com/s/sample10_math.pdf?raw=1",
    "Class 10 - Science": "https://www.dropbox.com/s/sample10_science.pdf?raw=1",
    "Class 12 - Physics": "https://www.dropbox.com/s/sample12_physics.pdf?raw=1",
    "Class 12 - Chemistry": "https://www.dropbox.com/s/sample12_chemistry.pdf?raw=1"
}

# Welcome message on bot start
async def start(update: Update, context: CallbackContext) -> None:
    welcome_text = (
        "👋 Welcome to the **Past Year Question Paper Bot**!\n\n"
        "📚 Available Commands:\n"
        "/papers - View available question papers\n"
        "/help - Get help"
    )
    await update.message.reply_text(welcome_text)

    # Automatically show the question paper menu after the welcome message
    await papers(update, context)


# Show available question papers
async def papers(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton(name, callback_data=name)]
        for name in question_papers.keys()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("📋 Select a question paper to download:", reply_markup=reply_markup)

# Handle paper selection
async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    paper_name = query.data
    if paper_name in question_papers:
        await query.message.reply_text(f"📄 Here’s your paper: {question_papers[paper_name]}")
    else:
        await query.message.reply_text("❌ Paper not found. Try again!")

# Main function
def main():
    TOKEN = "7915753271:AAECDi-zTsSXWKzgzII77nMJL7cx_XZFOjg"

    # Using ApplicationBuilder for v20+
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("papers", papers))
    app.add_handler(CallbackQueryHandler(button))

    print("✅ Bot is running... Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == '__main__':
    main()
