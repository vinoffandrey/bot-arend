# -*- coding: utf-8 -*-
import telebot
import telegram

from telebot import types
from telegram import Bot
from telegram import ParseMode

bot = telebot.TeleBot('5593941690:AAFQoJk6EfEJ_gi36G00sDINc_hGXpFZlrI')


###########################################################################################################################################################################
#Переменные для записи
city = ''
date = ''
link = ''
description = ''
city_arend = 0
adress = ''
people_arend = 0
contacts = ''
numberAvito = 0
idAvito = 0
rooms = 0
photo = []
cost_arend = 0
min_arend = 0
max_arend = 0
people = 0
cost = 0

@bot.message_handler(content_types=['text'])
def start(message):
	if message.text == '/start':
		return bot.send_message(message.from_user.id, 'Если Вы арендодатель, введите команду /give, если Вы хотите снять квартиру, введите /search')

	elif message.text == '/search':
		bot.send_message(message.from_user.id, "Какой город Вас интересует? 1.Калининград 2.Зеленоградск 3.Светлогорск (Введите цифру)")
		bot.register_next_step_handler(message, get_city)

	elif message.text =='/give':
		bot.send_message(message.from_user.id, "Вставьте сюда ссылку на своё объявление в Avito")
		bot.register_next_step_handler(message, get_profile)

	else:
		return bot.send_message(message.from_user.id, 'Напишите /start')

###########################################################################################################################################################################
#Логика арендодателя
def get_profile(message):
	global link
	link = message.text
	profile = open("img/profile.png", 'rb')
	bot.send_message(message.from_user.id, 'Напишите свой номер профиля в Личном кабинете Авито (только цифры)')
	bot.send_photo(message.from_user.id, profile)
	bot.register_next_step_handler(message, get_idAvito)

def get_idAvito(message):
	global numberAvito
	while numberAvito == 0: #проверяем что потолок цены изменился
		try:
			numberAvito = int(message.text) #проверяем, что возраст введен корректно
		except Exception:
			bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
			return get_profile(message)
	photoAvito = open("img/number.jpg", 'rb')
	bot.send_message(message.from_user.id, 'Напишите идентификатор объявления с Авито (только цифры)')
	bot.send_photo(message.from_user.id, photoAvito)
	bot.register_next_step_handler(message, get_link)

def get_link(message):
	global idAvito
	while idAvito == 0: #проверяем что потолок цены изменился
		try:
			idAvito = int(message.text) #проверяем, что возраст введен корректно
		except Exception:
			bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
			return get_idAvito(message)
	bot.send_message(message.from_user.id, 'Добавьте описание своей недвижимости')
	bot.register_next_step_handler(message, get_rooms)

def get_rooms(message):
	global description
	description = message.text
	bot.send_message(message.from_user.id, 'Сколько у Вас комнат?')
	bot.register_next_step_handler(message, get_photo)

def get_photo(message):
	global rooms
	while rooms == 0:
		try: 
			rooms = int(message.text)
			if rooms == 1:
				bot.send_message(message.from_user.id, 'Загрузите максимум 3 фотографии своей недвижимости: комната, кухня, санузел')
				bot.register_next_step_handler(message, get_description)
			elif rooms > 1:
				bot.send_message(message.from_user.id, 'Загрузите максимум 5 фотографий своей недвижимости: вид каждой комнаты, кухня, санузел')
				bot.register_next_step_handler(message, get_description)
			else:
				bot.send_message(message.from_user.id, 'Укажите правильное количество комнат')
				return get_rooms(message)
		except Exception:
			bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
			return get_rooms(message)

def get_description(message):
	global photo
	photo = message.text
	bot.send_message(message.from_user.id, f'В каком городе расположена недвижимость? \n 1.Калининград \n2.Зеленоградск \n3.Светлогорск (Введите цифру)')
	bot.register_next_step_handler(message, get_city_arend)

def get_city_arend(message):
	global city_arend
	while city_arend == 0: #проверяем что потолок цены изменился
		try:
			city_arend = int(message.text) #проверяем, что возраст введен корректно
		except Exception:
			bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
			return get_description(message)
	bot.send_message(message.from_user.id, 'Добавьте адрес недвижимости')
	bot.register_next_step_handler(message, get_adress)

def get_adress(message):
	global adress
	adress = message.text
	bot.send_message(message.from_user.id, 'Сколько человек вмещает Ваша недвижимость?')
	bot.register_next_step_handler(message, get_people_arend)

def get_people_arend(message):
	global people_arend
	while people_arend == 0: #проверяем что потолок цены изменился
		try:
			people_arend = int(message.text) #проверяем, что возраст введен корректно
		except Exception:
			bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
			return get_adress(message)
	bot.send_message(message.from_user.id, 'Цена за сутки')
	bot.register_next_step_handler(message, get_cost_arend)

def get_cost_arend(message):
	global cost_arend
	while cost_arend == 0: #проверяем что потолок цены изменился
		try:
			cost_arend = int(message.text) #проверяем, что возраст введен корректно
		except Exception:
			bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
			return get_people_arend(message)
	bot.send_message(message.from_user.id, 'Минимальный срок аренды')
	bot.register_next_step_handler(message, get_min_arend)

def get_min_arend(message):
	global min_arend
	while min_arend == 0: #проверяем что потолок цены изменился
		try:
			min_arend = int(message.text) #проверяем, что возраст введен корректно
		except Exception:
			bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
			return get_cost_arend(message)
	bot.send_message(message.from_user.id, 'Максимальный срок аренды')
	bot.register_next_step_handler(message, get_max_arend)

def get_max_arend(message):
	global max_arend
	while max_arend == 0: #проверяем что потолок цены изменился
		try:
			max_arend = int(message.text) #проверяем, что возраст введен корректно
		except Exception:
			bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
			return get_min_arend(message)
	bot.send_message(message.from_user.id, 'Введите ваши контакты (номер телефона, ссылка на телеграм)')
	bot.register_next_step_handler(message, get_contacts)


#Вывод введённой информации
def get_contacts(message):
	global contacts
	contacts = message.text
	bot.send_message(message.from_user.id, 'Проверьте, пожалуйста, заполненные Вами данные')
	text_contacts = f'Ссылка на авито {link} \n \
	Ваш номер профиля на Авито: {numberAvito} \n \
	Ваш идентификатор объявления на Авито: {idAvito} \n \
	________________________________________________________ \n \
		\n \
	Описание: {description} \n \
	________________________________________________________ \n \
		\n \
	Количество комнат: {rooms} \n \
	Фотографии недвижимости: {photo} \n \
	________________________________________________________ \n \
		\n \
	Город: {city_arend} \n \
	Адрес: {adress} \n \
	________________________________________________________ \n \
		\n \
	Вместимость: {people_arend} человек \n \
	Цена за сутки: {cost_arend} \n \
	________________________________________________________ \n \
		\n \
	Минимальный срок аренды: {min_arend} \n \
	Максимальный срок аренды: {max_arend} \n \
	________________________________________________________ \n \
		\n \
	Ваши контакты: {contacts}'
	bot.send_message(message.from_user.id, 'Всё верно?')
	keyboard_contacts = types.InlineKeyboardMarkup() #наша клавиатура
	key_post = types.InlineKeyboardButton(text='Опубликовать объявление', callback_data='post')
	keyboard_contacts.add(key_post) #добавляем кнопку в клавиатуру
	key_redakt= types.InlineKeyboardButton(text='Отредактировать объявление', callback_data='redukt')
	keyboard_contacts.add(key_redakt)
	key_delete= types.InlineKeyboardButton(text='Удалить объявление', callback_data='delete')
	keyboard_contacts.add(key_delete)
	bot.send_message(message.from_user.id, text=text_contacts, reply_markup=keyboard_contacts)


###########################################################################################################################################################################
#Логика арендатора
def get_city(message): #получаем город
	global city
	city = message.text
	bot.send_message(message.from_user.id, 'Какие даты Вас интуресуют? Напишите в формате: 11.05.2022-12.05.2022')
	bot.register_next_step_handler(message, get_date)

def get_date(message): #получаем даты
	global date
	date = message.text
	bot.send_message(message.from_user.id, 'Напишите количество гостей')
	bot.register_next_step_handler(message, get_people)

def get_people(message): #получаем количество людей
	global people
	people = message.text
	bot.send_message(message.from_user.id, 'Какой потолок цены Вас интересует? Напишите в формате: 2000')
	bot.register_next_step_handler(message, get_cost)

def get_cost(message): #получаем потолок цены
	global cost
	while cost == 0: #проверяем что потолок цены изменился
		try:
			cost = int(message.text) #проверяем, что возраст введен корректно
		except Exception:
			bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
	keyboard = types.InlineKeyboardMarkup() #наша клавиатура
	key_yes = types.InlineKeyboardButton(text='Подобрать варианты', callback_data='yes') #кнопка «Да»
	keyboard.add(key_yes) #добавляем кнопку в клавиатуру
	key_no= types.InlineKeyboardButton(text='Повторить заполнение', callback_data='no')
	keyboard.add(key_no)
	question = 'Вы выбрали город '+city+' на даты '+str(date)+' планирует заезжать '+str(people)+' человек. Потолок цены составляет: '+str(cost)+' рублей'
	bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


###########################################################################################################################################################################
#Обработчик событий по кнопкам
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
	if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
		#код сохранения данных, или их обработки
		all_variations(call.message)
	elif call.data == "no":
		bot.send_message(call.message.chat.id, 'Введите команду /start')#переспрашиваем
	elif call.data == "all":
		bot.send_message(call.message.chat.id, 'Здесь выводятся все квартиры')
	elif call.data == "min":
		bot.send_message(call.message.chat.id, 'Здесь выводятся по возрастанию цены')
	elif call.data == "search":
		bot.send_message(call.message.chat.id, 'Введите команду /start')
	elif call.data == "post":
		bot.send_message(call.message.chat.id, 'Объявление опубликовано')
		bot.send_message(call.message.chat.id, 'Чтобы вернуться к началу, напишите /start')
	elif call.data == "redukt":
		redukt_get_profile(call.message)
	elif call.data == "delete":
		bot.send_message(call.message.chat.id, 'Чтобы вернуться к началу, напишите /start')
	
	#Обработчик событий кнопок при редактировании контента Все ответы "Да"
	elif call.data == "get_profile_yes":
		redukt_get_idAvito(call.message)
	elif call.data == "get_idAvito_yes":
		redukt_get_link(call.message)
	elif call.data == "get_link_yes":
		redukt_get_rooms(call.message)
	elif call.data == "get_rooms_yes":
		redukt_get_photo(call.message)
	elif call.data == "get_photo_yes":
		redukt_get_description(call.message)
	elif call.data == "get_description_yes":
		redukt_get_city_arend(call.message)
	elif call.data == "get_city_arend_yes":
		redukt_get_adress(call.message)
	elif call.data == "get_adress_yes":
		redukt_get_people_arend(call.message)
	elif call.data == "get_people_arend_yes":
		redukt_get_cost_arend(call.message)
	elif call.data == "get_cost_arend_yes":
		redukt_get_min_arend(call.message)
	elif call.data == "get_min_arend_yes":
		redukt_get_max_arend(call.message)
	elif call.data == "get_max_arend_yes":
		redukt_get_contacts(call.message)
	elif call.data == "get_contacts_yes":
		redukt_get_contacts_final(call.message)

	#Обработчик событий кнопок при редактировании контента Все ответы "Нет"
	elif call.data == "get_profile_no":
		bot.send_message(call.message.chat.id, "Вставьте сюда ссылку на своё объявление в Avito")
		bot.register_next_step_handler(call.message, rewrite_get_profile)
	elif call.data == "get_idAvito_no":
		bot.send_message(call.message.chat.id, "Вставьте сюда номер профиля Авито (только цифры)")
		bot.register_next_step_handler(call.message, rewrite_get_idAvito)
	elif call.data == "get_link_no":
		bot.send_message(call.message.chat.id, "Вставьте сюда идентификатор объявления Авито (только цифры)")
		bot.register_next_step_handler(call.message, rewrite_get_link)
	elif call.data == "get_rooms_no":
		bot.send_message(call.message.chat.id, "Вставьте сюда описание")
		bot.register_next_step_handler(call.message, rewrite_get_rooms)
	elif call.data == "get_photo_no":
		bot.send_message(call.message.chat.id, "Вставьте сюда количество комнат (только цифры)")
		bot.register_next_step_handler(call.message, rewrite_get_photo)
	elif call.data == "get_description_no":
		bot.send_message(call.message.chat.id, "Вставьте сюда фотографии")
		bot.register_next_step_handler(call.message, rewrite_get_description)
	elif call.data == "get_city_arend_no":
		bot.send_message(call.message.chat.id, "Вставьте сюда город \n 1.Калининград \n2.Зеленоградск \n3.Светлогорск (Введите цифру)")
		bot.register_next_step_handler(call.message, rewrite_get_city_arend)
	elif call.data == "get_adress_no":
		bot.send_message(call.message.chat.id, "Вставьте сюда адрес")
		bot.register_next_step_handler(call.message, rewrite_get_adress)
	elif call.data == "get_people_arend_no":
		bot.send_message(call.message.chat.id, "Вставьте сюда количество человек (только цифры)")
		bot.register_next_step_handler(call.message, rewrite_get_people_arend)
	elif call.data == "get_cost_arend_no":
		bot.send_message(call.message.chat.id, "Вставьте сюда цену за сутки (только цифры)")
		bot.register_next_step_handler(call.message, rewrite_get_cost_arend)
	elif call.data == "get_min_arend_no":
		bot.send_message(call.message.chat.id, "Вставьте сюда минимальный срок аренды (только цифры)")
		bot.register_next_step_handler(call.message, rewrite_get_min_arend)
	elif call.data == "get_max_arend_no":
		bot.send_message(call.message.chat.id, "Вставьте сюда максимальный срок аренды (только цифры)")
		bot.register_next_step_handler(call.message, rewrite_get_max_arend)
	elif call.data == "get_contacts_no":
		bot.send_message(call.message.chat.id, "Вставьте сюда контакты")
		bot.register_next_step_handler(call.message, rewrite_get_contacts)

	else:
		bot.send_message(call.message.chat.id, 'Нажмите на нужную кнопку')

#Перезапись значений в БД
def rewrite_get_profile(message):
	global link
	link = message.text
	redukt_get_profile(message)
def rewrite_get_idAvito(message):
	global numberAvito
	numberAvito = message.text
	redukt_get_idAvito(message)
def rewrite_get_link(message):
	global idAvito
	idAvito = message.text
	redukt_get_link(message)
def rewrite_get_rooms(message):
	global description
	description = message.text
	redukt_get_rooms(message)
def rewrite_get_photo(message):
	global rooms
	rooms = message.text
	redukt_get_photo(message)
def rewrite_get_description(message):
	global photo
	photo = message.text
	redukt_get_description(message)
def rewrite_get_city_arend(message):
	global city_arend
	city_arend = message.text
	redukt_get_city_arend(message)
def rewrite_get_adress(message):
	global adress
	adress = message.text
	redukt_get_adress(message)
def rewrite_get_people_arend(message):
	global people_arend
	people_arend = message.text
	redukt_get_people_arend(message)
def rewrite_get_cost_arend(message):
	global cost_arend
	cost_arend = message.text
	redukt_get_cost_arend(message)
def rewrite_get_min_arend(message):
	global min_arend
	min_arend = message.text
	redukt_get_min_arend(message)
def rewrite_get_max_arend(message):
	global max_arend
	max_arend = message.text
	redukt_get_max_arend(message)
def rewrite_get_contacts(message):
	global contacts
	contacts = message.text
	redukt_get_contacts(message)


def redukt_get_profile(message):
	bot.send_message(message.chat.id, text = f'Ссылка на Авито: <a href="{link}">{link}</a>', parse_mode=telegram.ParseMode.HTML)
	question_profile = 'Всё верно?'
	keyboard_profile = types.InlineKeyboardMarkup() #наша клавиатура
	get_profile_yes = types.InlineKeyboardButton(text='Да', callback_data='get_profile_yes') #кнопка «Да»
	keyboard_profile.add(get_profile_yes) #добавляем кнопку в клавиатуру
	get_profile_no= types.InlineKeyboardButton(text='Нет', callback_data='get_profile_no')
	keyboard_profile.add(get_profile_no)
	bot.send_message(message.chat.id, text=question_profile, reply_markup=keyboard_profile)

def redukt_get_idAvito(message):
	bot.send_message(message.chat.id, text = f'Номер профиля Авито: <i>{numberAvito}</i>', parse_mode=telegram.ParseMode.HTML)
	question_idAvito = 'Всё верно?'
	keyboard_idAvito = types.InlineKeyboardMarkup() #наша клавиатура
	get_idAvito_yes = types.InlineKeyboardButton(text='Да', callback_data='get_idAvito_yes') #кнопка «Да»
	keyboard_idAvito.add(get_idAvito_yes) #добавляем кнопку в клавиатуру
	get_idAvito_no= types.InlineKeyboardButton(text='Нет', callback_data='get_idAvito_no')
	keyboard_idAvito.add(get_idAvito_no)
	bot.send_message(message.chat.id, text=question_idAvito, reply_markup=keyboard_idAvito)

def redukt_get_link(message):
	bot.send_message(message.chat.id, text = f'Идентификатор объявления Авито: <i>{idAvito}</i>', parse_mode=telegram.ParseMode.HTML)
	question_link = 'Всё верно?'
	keyboard_link = types.InlineKeyboardMarkup() #наша клавиатура
	get_link_yes = types.InlineKeyboardButton(text='Да', callback_data='get_link_yes') #кнопка «Да»
	keyboard_link.add(get_link_yes) #добавляем кнопку в клавиатуру
	get_link_no= types.InlineKeyboardButton(text='Нет', callback_data='get_link_no')
	keyboard_link.add(get_link_no)
	bot.send_message(message.chat.id, text=question_link, reply_markup=keyboard_link)

def redukt_get_rooms(message):
	bot.send_message(message.chat.id, text = f'Описание: <i>{description}</i>', parse_mode=telegram.ParseMode.HTML)
	question_rooms = 'Всё верно?'
	keyboard_rooms = types.InlineKeyboardMarkup() #наша клавиатура
	get_rooms_yes = types.InlineKeyboardButton(text='Да', callback_data='get_rooms_yes') #кнопка «Да»
	keyboard_rooms.add(get_rooms_yes) #добавляем кнопку в клавиатуру
	get_rooms_no= types.InlineKeyboardButton(text='Нет', callback_data='get_rooms_no')
	keyboard_rooms.add(get_rooms_no)
	bot.send_message(message.chat.id, text=question_rooms, reply_markup=keyboard_rooms)

def redukt_get_photo(message):
	bot.send_message(message.chat.id, text = f'Сколько комнат: <i>{rooms}</i>', parse_mode=telegram.ParseMode.HTML)
	question_photo = 'Всё верно?'
	keyboard_photo = types.InlineKeyboardMarkup() #наша клавиатура
	get_photo_yes = types.InlineKeyboardButton(text='Да', callback_data='get_photo_yes') #кнопка «Да»
	keyboard_photo.add(get_photo_yes) #добавляем кнопку в клавиатуру
	get_photo_no= types.InlineKeyboardButton(text='Нет', callback_data='get_photo_no')
	keyboard_photo.add(get_photo_no)
	bot.send_message(message.chat.id, text=question_photo, reply_markup=keyboard_photo)

def redukt_get_description(message):
	bot.send_message(message.chat.id, text = f'Фотографии: {photo}', parse_mode=telegram.ParseMode.HTML)
	question_description = 'Всё верно?'
	keyboard_dectiprion = types.InlineKeyboardMarkup() #наша клавиатура
	get_description_yes = types.InlineKeyboardButton(text='Да', callback_data='get_description_yes') #кнопка «Да»
	keyboard_dectiprion.add(get_description_yes) #добавляем кнопку в клавиатуру
	get_description_no= types.InlineKeyboardButton(text='Нет', callback_data='get_description_no')
	keyboard_dectiprion.add(get_description_no)
	bot.send_message(message.chat.id, text=question_description, reply_markup=keyboard_dectiprion)

def redukt_get_city_arend(message):
	bot.send_message(message.chat.id, text = f'Город: <i>{city_arend}</i>', parse_mode=telegram.ParseMode.HTML)
	question_arend = 'Всё верно?'
	keyboard_arend = types.InlineKeyboardMarkup() #наша клавиатура
	get_city_arend_yes = types.InlineKeyboardButton(text='Да', callback_data='get_city_arend_yes') #кнопка «Да»
	keyboard_arend.add(get_city_arend_yes) #добавляем кнопку в клавиатуру
	get_city_arend_no= types.InlineKeyboardButton(text='Нет', callback_data='get_city_arend_no')
	keyboard_arend.add(get_city_arend_no)
	bot.send_message(message.chat.id, text=question_arend, reply_markup=keyboard_arend)

def redukt_get_adress(message):
	bot.send_message(message.chat.id, text = f'Адрес: <i>{adress}</i>', parse_mode=telegram.ParseMode.HTML)
	question_adress = 'Всё верно?'
	keyboard_adress = types.InlineKeyboardMarkup() #наша клавиатура
	get_adress_yes = types.InlineKeyboardButton(text='Да', callback_data='get_adress_yes') #кнопка «Да»
	keyboard_adress.add(get_adress_yes) #добавляем кнопку в клавиатуру
	get_adress_no= types.InlineKeyboardButton(text='Нет', callback_data='get_adress_no')
	keyboard_adress.add(get_adress_no)
	bot.send_message(message.chat.id, text=question_adress, reply_markup=keyboard_adress)

def redukt_get_people_arend(message):
	bot.send_message(message.chat.id, text = f'Количество человек: <i>{people_arend}</i>', parse_mode=telegram.ParseMode.HTML)
	question_people = 'Всё верно?'
	keyboard_people = types.InlineKeyboardMarkup() #наша клавиатура
	get_people_arend_yes = types.InlineKeyboardButton(text='Да', callback_data='get_people_arend_yes') #кнопка «Да»
	keyboard_people.add(get_people_arend_yes) #добавляем кнопку в клавиатуру
	get_people_arend_no= types.InlineKeyboardButton(text='Нет', callback_data='get_people_arend_no')
	keyboard_people.add(get_people_arend_no)
	bot.send_message(message.chat.id, text=question_people, reply_markup=keyboard_people)

def redukt_get_cost_arend(message):
	bot.send_message(message.chat.id, text = f'Цена за сутки: <i>{cost_arend}</i>', parse_mode=telegram.ParseMode.HTML)
	question_cost = 'Всё верно?'
	keyboard_cost = types.InlineKeyboardMarkup() #наша клавиатура
	get_cost_arend_yes = types.InlineKeyboardButton(text='Да', callback_data='get_cost_arend_yes') #кнопка «Да»
	keyboard_cost.add(get_cost_arend_yes) #добавляем кнопку в клавиатуру
	get_cost_arend_no= types.InlineKeyboardButton(text='Нет', callback_data='get_cost_arend_no')
	keyboard_cost.add(get_cost_arend_no)
	bot.send_message(message.chat.id, text=question_cost, reply_markup=keyboard_cost)

def redukt_get_min_arend(message):
	bot.send_message(message.chat.id, text = f'Минимальный срок аренды: <i>{min_arend}</i>', parse_mode=telegram.ParseMode.HTML)
	question_min = 'Всё верно?'
	keyboard_min = types.InlineKeyboardMarkup() #наша клавиатура
	get_min_arend_yes = types.InlineKeyboardButton(text='Да', callback_data='get_min_arend_yes') #кнопка «Да»
	keyboard_min.add(get_min_arend_yes) #добавляем кнопку в клавиатуру
	get_min_arend_no= types.InlineKeyboardButton(text='Нет', callback_data='get_min_arend_no')
	keyboard_min.add(get_min_arend_no)
	bot.send_message(message.chat.id, text=question_min, reply_markup=keyboard_min)

def redukt_get_max_arend(message):
	bot.send_message(message.chat.id, text = f'Максимальный срок аренды: <i>{max_arend}</i>', parse_mode=telegram.ParseMode.HTML)
	question_max = 'Всё верно?'
	keyboard_max = types.InlineKeyboardMarkup() #наша клавиатура
	get_max_arend_yes = types.InlineKeyboardButton(text='Да', callback_data='get_max_arend_yes') #кнопка «Да»
	keyboard_max.add(get_max_arend_yes) #добавляем кнопку в клавиатуру
	get_max_arend_no= types.InlineKeyboardButton(text='Нет', callback_data='get_max_arend_no')
	keyboard_max.add(get_max_arend_no)
	bot.send_message(message.chat.id, text=question_max, reply_markup=keyboard_max)

def redukt_get_contacts(message):
	bot.send_message(message.chat.id, text = f'Контакты: <i>{contacts}</i>', parse_mode=telegram.ParseMode.HTML)
	question_contacts = 'Всё верно?'
	keyboard_contacts = types.InlineKeyboardMarkup() #наша клавиатура
	get_contacts_yes = types.InlineKeyboardButton(text='Да', callback_data='get_contacts_yes') #кнопка «Да»
	keyboard_contacts.add(get_contacts_yes) #добавляем кнопку в клавиатуру
	get_contacts_no= types.InlineKeyboardButton(text='Нет', callback_data='get_contacts_no')
	keyboard_contacts.add(get_contacts_no)
	bot.send_message(message.chat.id, text=question_contacts, reply_markup=keyboard_contacts)




def all_variations(message):
	# bot.send_message(message.chat.id, 'Новый шаг')
	keyboard2 = types.InlineKeyboardMarkup() #наша клавиатура
	key_all = types.InlineKeyboardButton(text='Показать все', callback_data='all') #кнопка «Да»
	keyboard2.add(key_all) #добавляем кнопку в клавиатуру
	key_min= types.InlineKeyboardButton(text='Показать по очереди, начиная с самой дешевой', callback_data='min')
	keyboard2.add(key_min)
	key_search= types.InlineKeyboardButton(text='Новый поиск', callback_data='search')
	keyboard2.add(key_search)  
	question2 = 'Найдено 6 квартир'
	bot.send_message(message.chat.id, text=question2, reply_markup=keyboard2)


def redukt_get_contacts_final(message):
	bot.send_message(message.chat.id, 'Проверьте, пожалуйста, заполненные Вами данные')
	text_contacts = f'Ссылка на авито {link} \n \
	Ваш номер профиля на Авито: {numberAvito} \n \
	Ваш идентификатор объявления на Авито: {idAvito} \n \
	________________________________________________________ \n \
		\n \
	Описание: {description} \n \
	________________________________________________________ \n \
		\n \
	Количество комнат: {rooms} \n \
	Фотографии недвижимости: {photo} \n \
	________________________________________________________ \n \
		\n \
	Город: {city_arend} \n \
	Адрес: {adress} \n \
	________________________________________________________ \n \
		\n \
	Вместимость: {people_arend} человек \n \
	Цена за сутки: {cost_arend} \n \
	________________________________________________________ \n \
		\n \
	Минимальный срок аренды: {min_arend} \n \
	Максимальный срок аренды: {max_arend} \n \
	________________________________________________________ \n \
		\n \
	Ваши контакты: {contacts}'
	bot.send_message(message.chat.id, 'Всё верно?')
	keyboard_contacts = types.InlineKeyboardMarkup() #наша клавиатура
	key_post = types.InlineKeyboardButton(text='Опубликовать объявление', callback_data='post')
	keyboard_contacts.add(key_post) #добавляем кнопку в клавиатуру
	key_redakt= types.InlineKeyboardButton(text='Отредактировать объявление', callback_data='redukt')
	keyboard_contacts.add(key_redakt)
	key_delete= types.InlineKeyboardButton(text='Удалить объявление', callback_data='delete')
	keyboard_contacts.add(key_delete)
	bot.send_message(message.chat.id, text=text_contacts, reply_markup=keyboard_contacts)



bot.polling(none_stop=True, interval=0)
