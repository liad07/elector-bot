from telegram.ext import *
import resposnses as Res

print("Bot started")
def start_command(update, context):
    update.message.reply_text('enter id or name')
def handle_message(update, context):
    text = str(update.message.text).lower()
    resposnses = Res.sample_res(text)
    update.message.reply_text(resposnses)



def main():
    updater = Updater("5485679484:AAHG2M5g3WGpZ3Yib5i21GdXcj2ZiPMRoOs", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling()
    updater.idle()


main()