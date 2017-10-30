import os
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters

# Вставьте в кавычки токен, полученный вами у BotFather.
TOKEN = os.environ['TOKEN']


def start(bot, update):
    """
    Функция, обрабатывающая начало диалога с ботом. Она говорит боту отправить пользователю текстовое сообщение,
    которое мы запишем в переменную text.
    """
    chat_id = update.message.chat_id
    text = 'Hello, I am The Real Talk Bot!'
    bot.send_message(chat_id=chat_id, text=text)


def echo(bot, update):
    """
    Функция, обрабатывающая начало диалога с ботом. Она говорит боту отправить пользователю текстовое сообщение,
    которое мы запишем в переменную text.
    """
    chat_id = update.message.chat_id
    text = update.message.text
    bot.send_message(chat_id=chat_id, text=text)


def main():
    """
    Основная функция программы, в которой производится основная настройка и запуск бота
    """

    # Создаем объект updater. updater играет роль приемника всех обновлений, которые отправляет Telegram.
    # Например когда пользователь отправляет сообщение боту, Telegram отправит обновление объекту updater, в котором
    # будет храниться вся информация об этом сообщении (chat_id, text и т.д.).
    updater = Updater(token=TOKEN)

    # updater автоматически создает dispatcher, который мы сохраняем в отдельную переменную. dispatcher выполняет роль
    # обработчика событий, который ему передает updater.
    dispatcher = updater.dispatcher

    # Создаем обработчик команды start, который будет обрабатывать первое сообщение пользователя
    start_handler = CommandHandler('start', start)

    # Создаем обработчик всех текстовых сообщений
    echo_handler = MessageHandler(Filters.text, echo)

    # Добавляем созданные обработчики в dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)

    # Запускаем прием всех обновлений с помощью updater
    updater.start_polling()


if __name__ == '__main__':
    # Запускаем основную функцию
    main()
