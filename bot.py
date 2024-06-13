import telebot

bot = telebot.TeleBot(tokem='7071355758:AAFmykdclGpnx5FoE_h_MpiUn5aq8wwdQ7Q')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я простой бот.")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Я могу ответить на команды /start и /help.")

bot.polling()