import telebot
from telebot import types
import random
token = "651334850:AAGCALC8yfsXez7vK_bzX8nzZZvzDpqYIX4"
telebot.apihelper.proxy = {'https': 'socks5://tvorogme:TyhoRuiGhj1874@tvorog.me:6666'}
 
# подключаемся к телеграму
 
bot = telebot.TeleBot(token=token)

sarcasmm = ['Советы от синего экрана монитора:  1. Нервные клетки не восстанавливаются.  2. Учи английский язык.  3. Настало время завести друга—программиста.', 'Программист: — Сегодня у сына день рождения. — И сколько ему исполняется? — 1024 дня.', 'Колобок повесился.', 'Случайно послушав 10 минут новости на арабском, ощутил острую необходимость что-нибудь взорвать.', 'Лена была за равноправие полов - поэтому ей наваляли как и мужу.', 'Вчера мой муж заявил моему отцу, что тот вырастил змею... На что папа с гордостью ответил, что вырастил не просто змею, а КОРОЛЕВСКУЮ КОБРУ!']
text_1 = ['Хочешь анекдот? Тогда отправь мне: /anek', 'Хватит мне писать. Я устал. Я иду спать.', 'XXXTENTANCION - ЖИВ!',' Рассольник - невкусный суп!']
# реагируем на команды /start и /help




@bot.message_handler(commands=['anek'])
def anek(message):
    f = random.randint(0,5)
    sarcasm = sarcasmm[f]
    user = message.chat.id
    bot.send_message(user, sarcasm)
@bot.message_handler(commands=['eight'])
def eight(message):
    user = message.chat.id
    bot.send_message(user, 'Без приказа Мстители работали неколлективно и не смогли защитить Землю. Конец!')
@bot.message_handler(commands=['seven'])
def seven(message):
    user = message.chat.id
    bot.send_message(user, 'Пока ты чилил Мстители спасли Землю, но тебя в спину убилподчинённый Локи. Конец!')
@bot.message_handler(commands=['six'])
def six(message):
    user = message.chat.id
    bot.send_message(user, 'Ты не смог их успокоить. Они разозлились ещё больше и переубивали друг друга, а Локи захватил Землю и привёл на неё Таноса! Конец!')
@bot.message_handler(commands=['five'])
def five(message):
    user = message.chat.id
    bot.send_message(user, 'Пока ты рассказывал свои планы на будущее, Локи со своей бандой напал на корабль. Правый двигатель отказал, надо отправить Кэпа(Капитана) и Тони(Жел.Человека) его чинить. Халк разозлился и пошёл громить остатки корабля, по-моему надо отправить Тора его остановить.')
    bot.send_message(user,  'Отправь: /seven, если отправишь всех всё делать, а сам будешь чилить. Отправь: /eight, если не будешь отдавать приказы и пойдёшь чилить.')
@bot.message_handler(commands=['four'])
def four(message):
    user = message.chat.id
    bot.send_message(user, 'Ты созвал всех выше перечисленных на корабль. С помощью Вижна и камня Разума ты развалил вражеское войско, а Т`Чалла смог закрыть портал, открытый Тессерактом. В итоге ты получил Тессеракт и стал использовать его в своих целях. Конец!')
@bot.message_handler(commands=['three'])
def three(message):
    user = message.chat.id
    bot.send_message(user, 'Ты созвал всех выше перечисленных на корабль. Но они не ладят друг с другом... Подозревают, что ты им что-то не договариваешь. Ну и на самом деле, Мстители тебе нужны, чтобы отобрать артефакт у Локи.')
    bot.send_message(user, 'Отправь: /five, если расскажешь им свой тайный замысел. Отправь: /six, если попытаешься их успокоить.')
@bot.message_handler(commands=['two'])
def two(message):
    user = message.chat.id
    bot.send_message(user, 'Так, ну секту мы собирём, но... ТЫ ЖЕ ЧЁРНЫЙ. КАКИЕ НАФИГ РАСИСТЫ? А? Ладно, раз ты такой РАСИСТ на тебе шутку: Какие у негра есть три белых вещи? Глаза, зубы и хозяин.')
    bot.send_message(user, 'Отправь: /kvest.')
@bot.message_handler(commands=['one'])
def one(message):
    user = message.chat.id
    bot.send_message(user, 'Мстители. Хорошее название, но мы же не мстить идём, а сражаться. Ладно...сойдёт. Какой состав?')
    bot.send_message(user, 'Отправь: /three, если хочешь собрать стандартную команду из: Капитана Америки, Халка, Железный Человек, Тор, Чёрная Вдова, Соколиный Глаз. Отправь: /four, если хочешь собрать другую тиму: Вижн, Росомаха, Т`Чалла, Доктор Стрэндж, Ртуть, Алая Ведьма')
@bot.message_handler(commands=['kvest'])
def kvest(message):
    user = message.chat.id
    bot.send_message(user, "Ты Ник Фьюри, директор Щ.И.Т. Тебе сообщают, что инопланетные войска собираются напасть на Землю. Надо собирать команду или секту?")
    bot.send_message(user, 'Отправь: /one, если собираем команду Мстители. Отправь: /two, если собираем секту Расистов.')
    
@bot.message_handler(commands=['start', 'help'])
def repeat_all_messages(message):
    # создаем клавиатуру
    keyboard = types.InlineKeyboardMarkup()

    # добавляем на нее две кнопки
    button1 = types.InlineKeyboardButton(text="Анекдоты", callback_data="button1")
    button2 = types.InlineKeyboardButton(text="Квест", callback_data="button2")
    keyboard.add(button1)
    keyboard.add(button2)
    bot.send_message(message.chat.id, "Выбирай!", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "button1":
            anek(call.message)
        if call.data == "button2":
            kvest(call.message)
        if call.data == "button3":
            one(call.message)
        if call.data == "button4":
            two(call.message)


#отправляем сообщение тому же пользователю с тем же текстом
# content_types=['text'] - сработает, есл им прислали текстовое сообщение
@bot.message_handler(content_types=['text'])
def echo(message):
    # message - входящее сообщение
    # message.text - это его текст
    # message.chat.id - это номер его автора
    #text = message.text
    d = random.randint(0,3)
    text = text_1[d]
    user = message.chat.id
    bot.send_message(user, text)
    
 
# поллинг - вечный цикл с обновлением входящих сообщений
bot.polling(none_stop=True)
