from golova import *
from telebot import types
import telebot
import threading
import _thread
import schedule
from bs4 import BeautifulSoup
import requests
import urllib.request as urllib2
import time
import threading
import _pickle as pickle
import flask
from flask import Flask

bot = telebot.TeleBot(token)

# TOKEN = '703423813:AAH3b6jnzRVlQn1gSCvgi8diMl5NkheLHGY'  ### Тут токен
# WEBHOOK_HOST = '185.86.76.74'  #### Тут IP
# WEBHOOK_PORT = 88  # 443, 80, 88 или 8443 (порт должен быть открыт!)
# WEBHOOK_LISTEN = '0.0.0.0'
#
# WEBHOOK_SSL_CERT = './webhook_cert.pem'
# WEBHOOK_SSL_PRIV = './webhook_pkey.pem'
#
# WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
# WEBHOOK_URL_PATH = "/%s/" % TOKEN
#
# app = Flask(__name__)
#
# bot = telebot.TeleBot(TOKEN)
#
#
# @app.route(WEBHOOK_URL_PATH, methods=['POST'])
# def webhook():
#     if flask.request.headers.get('content-type') == 'application/json':
#         json_string = flask.request.get_data().decode('utf-8')
#         update = telebot.types.Update.de_json(json_string)
#         bot.process_new_updates([update])
#         return ''
#     else:
#         flask.abort(403)


def get_html():
    r = requests.get('https://www.sports.ru/football/') #Менять ссылку тут
    return r.text

def get_html2():
    r = requests.get('https://www.sports.ru/basketball/') #Менять ссылку тут
    return r.text

def get_html3():
    r = requests.get('https://www.sports.ru/others/') #Менять ссылку тут
    return r.text

def test():

    soup = BeautifulSoup(get_html() , 'html.parser')
    content = soup.find('div', class_='page-layout')
    right_col = content.find('div', class_='columns-layout main-wrap')
    #print(right_col)
    news_list = right_col.find('main', class_='columns-layout__main material-list_last-item_border_none')
    article_list=news_list.find_all('article')
    art_list = [] #Лист со статьями
    i=0
    for article in article_list[0:5]:
        title = article.find('img')['alt']
        photo = article.find('img')['data-lazy-normal']
        link = article.find('a' ,class_='h2')['href']
        art_list.append([title,photo,link])
    # print(art_list)
    abc=art_list[1][0]
    abc2=art_list[0][0]
    abc3=art_list[2][0]
    # print(abc)
    # print(abc2)
    # print(abc3)
    set_ssd(1,art_list)
    return art_list

def test2():

    soup = BeautifulSoup(get_html2() , 'html.parser')
    content = soup.find('div', class_='page-layout')
    right_col = content.find('div', class_='columns-layout main-wrap')
    #print(right_col)
    news_list = right_col.find('main', class_='columns-layout__main material-list_last-item_border_none')
    article_list=news_list.find_all('article')
    art_list = [] #Лист со статьями
    i=0
    for article in article_list[0:5]:
        title = article.find('img')['alt']
        photo = article.find('img')['data-lazy-normal']
        link = article.find('a' ,class_='h2')['href']
        art_list.append([title,photo,link])
    # print(art_list)
    abc=art_list[1][0]
    abc2=art_list[0][0]
    abc3=art_list[2][0]
    # print(abc)
    # print(abc2)
    # print(abc3)
    set_ssd(2,art_list)
    return art_list

def test3():

    soup = BeautifulSoup(get_html3() , 'html.parser')
    content = soup.find('div', class_='page-layout')
    right_col = content.find('div', class_='columns-layout main-wrap')
    #print(right_col)
    news_list = right_col.find('main', class_='columns-layout__main material-list_last-item_border_none')
    article_list=news_list.find_all('article')
    art_list = [] #Лист со статьями
    i=0
    for article in article_list[0:5]:
        title = article.find('img')['alt']
        photo = article.find('img')['data-lazy-normal']
        link = article.find('a' ,class_='h2')['href']
        art_list.append([title,photo,link])
    # print(art_list)
    abc=art_list[1][0]
    abc2=art_list[0][0]
    abc3=art_list[2][0]
    # print(abc)
    # print(abc2)
    # print(abc3)
    set_ssd(3,art_list)
    return art_list

a = test()
print(a)


#bot = telebot.TeleBot(token)







@bot.message_handler(commands=['start'])

def handle_start(message):
    unique_code = extract_unique_code(message.text)
    if message.chat.username != None:
        urnme = message.chat.username
    else:
        try:
            urnme = message.chat.first_name + ' ' + +message.chat.last_name
        except Exception:
            urnme = message.chat.first_name
    if new_user(message.chat.id):
        if unique_code != None:
            if unique_code[:3] == 'REF':
                add_new_user_by_ref(message.chat.id,unique_code[3:],urnme)
                print(unique_code+' addsa')
                try:
                    helloadv = '[Пользователь](tg://user?id=' + str(message.chat.id) + ') '

                    #bot.send_message(unique_code[3:],'Вы пригласили '+helloadv, parse_mode='Markdown')
                    a=get_refS(unique_code[3:])
                    print(a)
                    set_refS(unique_code[3:],a)

                    referal(message.chat.id, unique_code[3:]) #эта функция добавляет в REF айдишник

                    #Прикол в том что это сообщение идет челику который позвал
                except Exception:
                    aa = 1
        else:
            add_new_user(message.chat.id, urnme)

        set_user_stage(message.chat.id, '')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                       ['Рефералы', 'Канал', 'Зарегистрироваться','Получить бонус','Eng','5 горячих новостей']])

        bot.send_message(message.from_user.id, 'Приветстви', parse_mode='HTML',
                         reply_markup=keyboard)
        return

    if message.chat.id<0: #это чек,пишут в бота либо в группу
        # bot.send_message(message.chat.id,'tlolololo')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                       ['Рефералы', 'Доставка', 'Тест', 'О нас']])
        bot.send_message(message.chat.id, 'Опа! Привет ты в группу'
                                          '\nТут всякие приколы будут теститься', parse_mode='HTML',
                         reply_markup=keyboard)
    else:
        check='https://t.me/' + 'XBet_News_bot' + '?start=REF' + str(message.chat.id)
        abc = message.text[10:]
        abc2 = message.chat.id
        print(abc)
        print(message.text)
        print(message.chat.id)
        if str(abc2)==str(abc):
            #abc=m.text[3:]
            bot.send_message(message.chat.id,'Вы уже подписаны')
            print(check)
        else:


        # bot.send_message(message.chat.id,'trtrtrtrt')
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                       ['Рефералы', 'Канал', 'Зарегистрироваться','Получить бонус','Eng','5 горячих новостей']])
            bot.send_message(message.from_user.id,'тут сылка на картинку')
            bot.send_message(message.from_user.id, 'Приветствие', parse_mode='HTML',
                         reply_markup=keyboard)








@bot.message_handler(commands=['admin'])
def admin(m):
    set_user_stage(m.chat.id,'in_admin')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['В главное меню']])
    msg = bot.send_message(m.chat.id, 'А вот и скрытая панель управления',reply_markup=keyboard)
    return()









@bot.callback_query_handler(func=lambda c:True)
def inline(c):
    stage = get_user_stage(c.message.chat.id)
    if c.data=='Окрошка':
        bot.answer_callback_query(c.id, 'Вы заказали ' + str(c.data))
    # if c.data=='Да':
    #     print('asd')
    if c.data[:4]=='jopa':
        print('opasya')








@bot.message_handler(content_types=['text'])
def name(m):
    stage = get_user_stage(m.chat.id)
    if stage == 'in_admin' and m.text == '12q3':
        set_user_stage(m.chat.id, 'admin')
        if new_admin(m.chat.id):
            add_new_superadmin(m.chat.id)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Рассылка']])
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['В главное меню']])
        msg = bot.send_message(m.chat.id, 'Пароль верный', reply_markup=keyboard)

    if m.text=='Рассылка':
        set_user_stage(m.chat.id, 'add_rassilka_12')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['В главное меню']])
        msg = bot.send_message(m.chat.id, 'Введите сообщение для рассылки', reply_markup=keyboard)

    if stage=='add_rassilka_12' and m.text!='В главное меню':
        set_user_stage(m.chat.id, '')
        threading.Thread(target=rassilka_text3, kwargs={'txt': m.text}).start()
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Рассылка']])
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['В главное меню']])
        msg = bot.send_message(m.chat.id, 'Ваше сообщение доставлено',reply_markup=keyboard)


#######################################################
    if m.text=='Eng':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                       ['Invite', 'Channel', 'Registration', 'Claim a Bonus','Menu', 'Rus']])
        bot.send_message(m.chat.id, 'Hello', parse_mode='HTML',
                         reply_markup=keyboard)

    if m.text=='Invite':
        print(str(get_ref(m.chat.id)))

        a = m.chat.first_name
        b = m.chat.last_name
        # print(a)
        # print(b)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                       ['Invite', 'Channel', 'Registration', 'Claim a Bonus','Rus']])
        c = get_refS(m.chat.id)
        botname = bot.get_me().username
        print(a)
        # helloadv = '[PAshka](tg://user?id=' + str(450216321) + ') '
        if b == None:
            if len(str(get_ref(m.chat.id))) == 0:
                helloadv = 'Вы пришли сами)'
                msg = bot.send_message(m.chat.id, 'You came yourself' + '\n' + 'Invited users: ' + str(c) + '\n'
                                                                                                                    'Your link:'
                # '\nhttps://t.me/'+'XBet_News_bot'+'?start=REF'+str(m.chat.id),
                                                                                                                    '\nhttps://t.me/' + 'XBet' + '_' + 'News' + '_' + 'bot' + '?start=REF' + str(
                    m.chat.id),

                                       #            '\nhttps://t.me/Plostibot?start=REF' + str(m.chat.id),
                                       reply_markup=keyboard)
                print(1)
            else:
                cc = get_ref(m.chat.id)
                print(cc)
                # чек name(ник) где id = ref(айдишник челикса)
                cc2 = get_nick(cc)
                print(cc2)
                # helloadv='[Пользователь](tg://user?id=' + str(get_ref(m.chat.id))+ ') '
                helloadv = '[' + str(cc2) + '](tg://user?id=' + str(get_ref(m.chat.id)) + ') '
                bot.send_message(m.chat.id, 'Invited you ' + helloadv, parse_mode='Markdown')
                msg = bot.send_message(m.chat.id, 'Invited users: ' + str(c) + '\n'
                                                                                          'Your link:'
                # '\nhttps://t.me/'+'XBet_News_bot'+'?start=REF'+str(m.chat.id),
                                                                                          '\nhttps://t.me/' + 'XBet' + '_' + 'News' + '_' + 'bot' + '?start=REF' + str(
                    m.chat.id),

                                       reply_markup=keyboard)
                print(2)
            print(str(get_ref(m.chat.id)))
        else:
            if len(str(get_ref(m.chat.id))) == 0:
                helloadv = 'Вы пришли сами)'
                msg = bot.send_message(m.chat.id, 'You came yourself' + '\n' + 'Invited users: ' + str(c) + '\n'
                                                                                                                    'Your link:'
                # '\nhttps://t.me/'+'XBet_News_bot'+'?start=REF'+str(m.chat.id),
                                                                                                                    '\nhttps://t.me/' + 'XBet' + '_' + 'News' + '_' + 'bot' + '?start=REF' + str(
                    m.chat.id),

                                       reply_markup=keyboard)
                print(3)
            else:
                cc = get_ref(m.chat.id)
                print(cc)
                # чек name(ник) где id = ref(айдишник челикса)
                cc2 = get_nick(cc)
                print(cc2)
                # helloadv = '['+str(a)+' '+str(b)+'](tg://user?id=' + str(get_ref(m.chat.id))+ ') '
                helloadv = '[' + str(cc2) + '](tg://user?id=' + str(get_ref(m.chat.id)) + ') '

                # helloadv='[Пользователь](tg://user?id=' + str(get_ref(m.chat.id))+ ') '
                bot.send_message(m.chat.id, 'Invited you ' + helloadv, parse_mode='Markdown')
                msg = bot.send_message(m.chat.id, 'Invited users: ' + str(c) + '\n'
                                                                                          'Your link:'
                # '\nhttps://t.me/'+'XBet_News_bot'+'?start=REF'+str(m.chat.id),
                                                                                          '\nhttps://t.me/' + 'XBet' + '_' + 'News' + '_' + 'bot' + '?start=REF' + str(
                    m.chat.id),

                                       reply_markup=keyboard)

                # helloadv = '['+str(a)+' '+str(b)+'](tg://user?id=' + str(get_ref(m.chat.id))+ ') '
                # нижняя рабочая строка ,над верхней работаю
                print(4)


    if m.text=='Channel':
        set_user_stage(m.chat.id, '')
        keyboardd = types.InlineKeyboardMarkup()

        url_button = types.InlineKeyboardButton(text="Channel here",
                                                url='https://t.me/joinchat/GtXBgUZY49sXh7NvjV1I-g')
        keyboardd.add(url_button)
        bot.send_message(m.from_user.id, 'Go to the channel',
                         parse_mode='HTML',
                         reply_markup=keyboardd)
        a = bot.get_me().username
        print(a)

    if m.text=='Registration':
        keyboardd = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Click",
                                                url="https://www.google.com")
        keyboardd.add(url_button)
        bot.send_message(m.chat.id, 'go to the registration site', reply_markup=keyboardd)

    if m.text=='Claim a Bonus':
        keyboardd = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Click",
                                                url="https://www.google.com")
        keyboardd.add(url_button)
        bot.send_message(m.chat.id,'Go to pick up bonuses',reply_markup=keyboardd)

    if m.text=='Menu':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                       ['Invite', 'Channel', 'Registration', 'Claim a Bonus', 'Rus']])
        bot.send_message(m.chat.id, 'Youre in the main menu', parse_mode='HTML',
                         reply_markup=keyboard)

    if m.text=='Rus':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                       ['Рефералы', 'Канал', 'Зарегистрироваться', 'Получить бонус', 'Eng', '5 горячих новостей']])
        bot.send_message(m.chat.id, 'Вы в главном меню', parse_mode='HTML',
                         reply_markup=keyboard)

#######################################################









    if m.text=='5 горячих новостей':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                       ['Футбол', 'Баскетбол', 'Общие','В главное меню']])
        bot.send_message(m.chat.id, 'Выберите категорию', reply_markup=keyboard)

    if m.text=='Футбол':
        # time.sleep(5)
        print(get_ssd(1))
        proba = get_ssd(1)[0][0]
        bot.send_message(m.chat.id,'<a href="'+get_ssd(1)[0][2]+'">'+get_ssd(1)[0][0]+'</a>',parse_mode='HTML')
        bot.send_message(m.chat.id,'<a href="'+get_ssd(1)[1][2]+'">'+get_ssd(1)[1][0]+'</a>',parse_mode='HTML')
        bot.send_message(m.chat.id,'<a href="'+get_ssd(1)[2][2]+'">'+get_ssd(1)[2][0]+'</a>',parse_mode='HTML')
        bot.send_message(m.chat.id,'<a href="'+get_ssd(1)[3][2]+'">'+get_ssd(1)[3][0]+'</a>',parse_mode='HTML')
        bot.send_message(m.chat.id,'<a href="'+get_ssd(1)[4][2]+'">'+get_ssd(1)[4][0]+'</a>',parse_mode='HTML')

    if m.text=='Баскетбол':
        bot.send_message(m.chat.id, '<a href="' + get_ssd(2)[0][2] + '">' + get_ssd(2)[0][0] + '</a>',
                         parse_mode='HTML')
        bot.send_message(m.chat.id, '<a href="' + get_ssd(2)[1][2] + '">' + get_ssd(2)[1][0] + '</a>',
                         parse_mode='HTML')
        bot.send_message(m.chat.id, '<a href="' + get_ssd(2)[2][2] + '">' + get_ssd(2)[2][0] + '</a>',
                         parse_mode='HTML')
        bot.send_message(m.chat.id, '<a href="' + get_ssd(2)[3][2] + '">' + get_ssd(2)[3][0] + '</a>',
                         parse_mode='HTML')
        bot.send_message(m.chat.id, '<a href="' + get_ssd(2)[4][2] + '">' + get_ssd(2)[4][0] + '</a>',
                         parse_mode='HTML')

    if m.text=='Общие':
        bot.send_message(m.chat.id, '<a href="' + get_ssd(3)[0][2] + '">' + get_ssd(3)[0][0] + '</a>',
                         parse_mode='HTML')
        bot.send_message(m.chat.id, '<a href="' + get_ssd(3)[1][2] + '">' + get_ssd(3)[1][0] + '</a>',
                         parse_mode='HTML')
        bot.send_message(m.chat.id, '<a href="' + get_ssd(3)[2][2] + '">' + get_ssd(3)[2][0] + '</a>',
                         parse_mode='HTML')
        bot.send_message(m.chat.id, '<a href="' + get_ssd(3)[3][2] + '">' + get_ssd(3)[3][0] + '</a>',
                         parse_mode='HTML')
        bot.send_message(m.chat.id, '<a href="' + get_ssd(3)[4][2] + '">' + get_ssd(3)[4][0] + '</a>',
                         parse_mode='HTML')





    if m.text=='В главное меню':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                       ['Рефералы', 'Канал', 'Зарегистрироваться', 'Получить бонус','Eng','5 горячих новостей']])
        bot.send_message(m.chat.id,'Вы в главном меню',reply_markup=keyboard)


    if m.text=='Зарегистрироваться':
        keyboardd = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Клик",
                                                url="https://www.google.com")
        keyboardd.add(url_button)
        bot.send_message(m.chat.id, 'Переходи на сайт для регистрации', reply_markup=keyboardd)

    if m.text=='Получить бонус':
        keyboardd = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Клик",
                                                url="https://www.google.com")
        keyboardd.add(url_button)
        bot.send_message(m.chat.id,'Переходи на сайт что бы забрать бонусы',reply_markup=keyboardd)


    if m.text=='Канал':
        set_user_stage(m.chat.id,'')
        keyboardd = types.InlineKeyboardMarkup()

        url_button = types.InlineKeyboardButton(text="Канал тут",
                                                url='https://t.me/joinchat/GtXBgUZY49sXh7NvjV1I-g')
        keyboardd.add(url_button)
        bot.send_message(m.from_user.id, 'Переходи в наш канал',
                         parse_mode='HTML',
                         reply_markup=keyboardd)
        a = bot.get_me().username
        print(a)

    if m.text =='Рефералы':
        print(str(get_ref(m.chat.id)))

        a = m.chat.first_name
        b = m.chat.last_name
        #print(a)
        #print(b)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                       ['Рефералы', 'Канал', 'Зарегистрироваться','Получить бонус','Eng','5 горячих новостей']])
        c=get_refS(m.chat.id)
        botname = bot.get_me().username
        print(a)
        #helloadv = '[PAshka](tg://user?id=' + str(450216321) + ') '
        if b==None:
            if len(str(get_ref(m.chat.id)))==0:
                helloadv = 'Вы пришли сами)'
                msg = bot.send_message(m.chat.id, 'Вы пришли сами'+'\n'+'Приглашено пользователей: '+str(c)+'\n'
                                                                              'А вот Ваша ссылка для приглашения друзей:'
                                                                                                            # '\nhttps://t.me/'+'XBet_News_bot'+'?start=REF'+str(m.chat.id),
                                       '\nhttps://t.me/' + 'XBet'+'_'+'News'+'_'+'bot' + '?start=REF' + str(m.chat.id),

                                       #            '\nhttps://t.me/Plostibot?start=REF' + str(m.chat.id),
                                       reply_markup=keyboard)
                print(1)
            else:
                cc = get_ref(m.chat.id)
                print(cc)
                # чек name(ник) где id = ref(айдишник челикса)
                cc2 = get_nick(cc)
                print(cc2)
                # helloadv='[Пользователь](tg://user?id=' + str(get_ref(m.chat.id))+ ') '
                helloadv = '[' + str(cc2) + '](tg://user?id=' + str(get_ref(m.chat.id)) + ') '
                bot.send_message(m.chat.id,'Вас пригласил '+helloadv, parse_mode='Markdown')
                msg = bot.send_message(m.chat.id, 'Приглашено пользователей: '+str(c)+'\n'
                                                                              'А вот Ваша ссылка для приглашения друзей:'
                                                                                                            # '\nhttps://t.me/'+'XBet_News_bot'+'?start=REF'+str(m.chat.id),
                                                                                                                       '\nhttps://t.me/' + 'XBet' + '_' + 'News' + '_' + 'bot' + '?start=REF' + str(
                    m.chat.id),

                                       reply_markup=keyboard)
                print(2)
            print(str(get_ref(m.chat.id)))
        else:
            if len(str(get_ref(m.chat.id)))==0:
                helloadv='Вы пришли сами)'
                msg = bot.send_message(m.chat.id, 'Вы пришли сами'+'\n'+'Приглашено пользователей: '+str(c)+'\n'
                                                                              'А вот Ваша ссылка для приглашения друзей:'
                                                                                                            # '\nhttps://t.me/'+'XBet_News_bot'+'?start=REF'+str(m.chat.id),
                                                                                                            '\nhttps://t.me/' + 'XBet' + '_' + 'News' + '_' + 'bot' + '?start=REF' + str(
                    m.chat.id),

                                       reply_markup=keyboard)
                print(3)
            else:
                cc = get_ref(m.chat.id)
                print(cc)
                # чек name(ник) где id = ref(айдишник челикса)
                cc2 = get_nick(cc)
                print(cc2)
                #helloadv = '['+str(a)+' '+str(b)+'](tg://user?id=' + str(get_ref(m.chat.id))+ ') '
                helloadv = '['+str(cc2)+'](tg://user?id=' + str(get_ref(m.chat.id))+ ') '

                #helloadv='[Пользователь](tg://user?id=' + str(get_ref(m.chat.id))+ ') '
                bot.send_message(m.chat.id,'Вас пригласил '+helloadv, parse_mode='Markdown')
                msg = bot.send_message(m.chat.id, 'Приглашено пользователей: '+str(c)+'\n'
                                                                              'А вот Ваша ссылка для приглашения друзей:'
                                                                                                            # '\nhttps://t.me/'+'XBet_News_bot'+'?start=REF'+str(m.chat.id),
                                                                                                                       '\nhttps://t.me/' + 'XBet' + '_' + 'News' + '_' + 'bot' + '?start=REF' + str(
                    m.chat.id),

                                       reply_markup=keyboard)

                #helloadv = '['+str(a)+' '+str(b)+'](tg://user?id=' + str(get_ref(m.chat.id))+ ') '
                #нижняя рабочая строка ,над верхней работаю
                print(4)








schedule.every(15).minutes.do(test)
schedule.every(15).minutes.do(test2)
schedule.every(15).minutes.do(test3)

def lal():
    while 1:
        schedule.run_pending()
        time.sleep(1)
_thread.start_new_thread(lal,())



def rassilka_text3(txt):# рассылка для админов
    admins=get_user_list_id()

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for i in range(0,len(admins)):
      try:
            try:
                msg = bot.send_message(admins[i], txt, parse_mode='Markdown')
            except Exception:
                msg = bot.send_message(admins[i], txt)

      except Exception:
        time.sleep(0.5)
      time.sleep(0.3)



# bot.remove_webhook()
#
# bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
#                 certificate=open(WEBHOOK_SSL_CERT, 'r'))
#
#
# app.run(host=WEBHOOK_LISTEN,
#         port=WEBHOOK_PORT,
#         ssl_context=(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV),
#         threaded=True)

if __name__ == '__main__':
    bot.polling(none_stop=True)
