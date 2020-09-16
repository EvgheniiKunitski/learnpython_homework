"""
Домашнее задание №1
Использование библиотек: ephem
* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.
"""
import logging, sys
import ephem
import settings
from datetime import date

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD
    }
}


def greet_user(update, context):
    logging.info("Called /start")
    update.message.reply_text("Привет, можешь запросить в каком созвездии находится сегодня, названная тобой, планета")
    update.message.reply_text("/planet Mercury, Venus, Mars, Jupiter, Saturn, Uranus, and Neptune")


def talk_to_me(update, context):
    logging.info("Called talk_to_me")
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def get_the_constellation(update, context):
    logging.info("Called /planet")
    user_planet = update.message.text.split()[1]
    logging.info(user_planet)
    today = date.today()
    if user_planet not in planets:
        update.message.reply_text("вы ошиблись в названии планеты")
        logging.error("Planet is spelled incorrectly")
    else:
        if user_planet == planets[0]:
            planet_request = ephem.Mercury(today)
        elif user_planet == planets[1]:
            planet_request = ephem.Venus(today)
        #elif user_planet == planets[2]:
        #    planet_request = ephem.Earth(today)
        #it is a place for exception, as Earth is point of view.
        elif user_planet == planets[3]:
            planet_request = ephem.Mars(today)
        elif user_planet == planets[4]:
            planet_request = ephem.Jupiter(today)
        elif user_planet == planets[5]:
            planet_request = ephem.Saturn(today)
        elif user_planet == planets[6]:
            planet_request = ephem.Uranus(today)
        else:
            planet_request = ephem.Neptune(today)
        const = ephem.constellation(planet_request)[1]
        reply = "Сегодя планета " + user_planet + " находится в созвездии " + const
        update.message.reply_text(reply)


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_the_constellation))
    #dp.add_handler(CommandHandler("quit", sys.exit()))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()
    

if __name__ == "__main__":
    main()