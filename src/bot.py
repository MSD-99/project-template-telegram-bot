import os

import telebot
from loguru import logger

from src.utils.constants import Keyboards
from src.utils.io import proxy, read_json, write_json


class Bot:
    """
    Template  for telegram bot.
    """
    def __init__(self) -> None:
        # self.proxy = '123.231.226.114:47562'
        # proxy(proxy_url=self.proxy, type='HTTPS')

        self.bot = telebot.TeleBot(os.environ['TELEGRAM_BOT_TMP_TOKEN'])
        self.echo_all = self.bot.message_handler(\
            func=lambda message: True)\
            (self.echo_all)

    def run(self):
        logger.info('Bot is running...')
        self.bot.infinity_polling()

    def echo_all(self, message):
        write_json(filename= 'messages.json', data=message.json, indent=4)
        self.bot.reply_to(message, message.text)
        self.bot.send_message(
            message.chat.id,
            message.text,
            reply_markup=Keyboards.main
            )

if __name__ == '__main__':
    logger.info('Bot started!')
    bot = Bot()
    bot.run()