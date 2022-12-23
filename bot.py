import telebot, datetime, pymysql
connection = pymysql.connect(host='localhost', user='root', password='root', database='sem9', cursorclass=pymysql.cursors.DictCursor)

print('Сегодня новые анкеты: ')
bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет. Это бот кадрового агенства, готовы заполнить анкету? /reg')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == '/reg':
        base = []
        base.append(message.from_user.id)
        base.append(message.from_user.username)
        bot.send_message(message.from_user.id, "Ваша фамилия?")
        bot.register_next_step_handler(message, reg_surname, base)

def reg_surname(message, base):
    base.append(message.text)
    bot.send_message(message.from_user.id, "Ваше имя?")
    bot.register_next_step_handler(message, reg_name, base)

def reg_name(message, base):
    base.append(message.text)
    bot.send_message(message.from_user.id, "Ваше отчество?")
    bot.register_next_step_handler(message, reg_first_name, base)

def reg_first_name(message, base):
    base.append(message.text)
    bot.send_message(message.from_user.id, "Сколько Вам лет?")
    bot.register_next_step_handler(message, reg_age, base)

def reg_age(message, base):
    digits = list(message.text)
    digits = ''.join([i for i in digits if i in '0123456789'])
    num = len(digits)
    if num < 3 and num > 0:
        base.append(int(digits))
    else:
        base.append(0)
    bot.send_message(message.from_user.id, "Ваш город?")
    bot.register_next_step_handler(message, reg_city, base)

def reg_city(message, base):
    base.append(message.text)
    bot.send_message(message.from_user.id, "Должность на которую Вы претендуете?")
    bot.register_next_step_handler(message, reg_post, base)

def reg_post(message, base):
    base.append(message.text)
    bot.send_message(message.from_user.id, "Желаемый уровень заработной платы?")
    bot.register_next_step_handler(message, reg_salary, base)

def reg_salary(message, base):
    digits = list(message.text)
    digits = ''.join([i for i in digits if i in '0123456789'])
    num = len(digits)
    if num < 7 and num > 0:
        base.append(int(digits))
    else:
        base.append(0)
    bot.send_message(message.from_user.id, "Ссылка на Ваше резюме?")
    bot.register_next_step_handler(message, reg_resume, base)

def reg_resume(message, base):
    base.append(message.text)
    bot.send_message(message.from_user.id, "Ссылка на Ваше портфолио?")
    bot.register_next_step_handler(message, reg_portfolio, base)

def reg_portfolio(message, base):
    base.append(message.text)

    with connection.cursor() as cursor:
        insert_query = "INSERT INTO `staff` (`surname`, `name`, `firs_name`, `years`, `city`, `post`, `salary`, `user_id`, `telegram`, `resume`, `portfolio`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(insert_query, (base[2], base[3], base[4], base[5], base[6], base[7], base[8], base[0], base[1], base[9], base[10]))
        connection.commit()


    bot.send_message(message.from_user.id, "Анкета заполнена. В ближайшее время с Вами свяжется менеджер.")
    now = datetime.datetime.now()
    print(now, base[0], base[1])

bot.polling()