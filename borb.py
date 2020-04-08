import telebot

bot = telebot.TeleBot("1176762963:AAE7gkFBRQLGon63_7MOBXgLrXwQG1IWkCs")


@bot.message_handler(commands=['start', 'help', 'settings'])
def send_welcome(message):
	bot.reply_to(message, "Assalomu Aleykum Boriga baraka kapital shuosining muxlisi.\nRasmiy guruhimizga (@boriga_baraka_shou_info) do'stlaringizni taklif qiling, \nAgarda taklif qilgan bo'lsangiz telefon raqamingizni jo'nating,\nMisol uchun +998901234567,\n!!!Agarda!!! siz guruhimizga do'stlaringizni taklif qilmagan bo'lsangiz raqamingiz ro'yxatdan o'tkazilmaydi")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if "+9989" in message.text:
        bot.reply_to(message, "Raxmat arizangiz qabul qilindi,\nRasmiy guruhimizga (@boriga_baraka_shou_info) do'stlaringizni taklif qilgan bo'lsangiz o'yinimizda ishtirok etish imkoniyatiga ega bo'lasiz!!!")
    else:
        bot.reply_to(message, "Iltimos botimiz bilan muloqot qilish uchun,\n/start\n/help\n/settings\nBuyruqlaridan foydalaning")
bot.polling()
