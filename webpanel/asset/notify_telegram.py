import telegram
from django.contrib.auth.models import User


class notifierClass:
    """
    Класс для отправки уведомлений от имени вашего бота
    https://github.com/kpimaker/telegram-notifier
    """

    def __init__(self, token='default'):
        self.bot = telegram.Bot(token)

    def send_notification(self, chat_id='', text="Default message!"):
        self.bot.sendMessage(chat_id=chat_id, text=text[:4000],
                             parse_mode="HTML")

    def send_sticker(self, chat='', sticker='default'):
        if sticker in self.config['stickers']:
            self.bot.sendSticker(chat_id=self.chat_id,
                                 sticker=self.config['stickers'][sticker])


def notify(text='Default notification message!'):
    notifier = notifierClass("439963554:AAGfPPViwLa_KVeGBOJFoIdsO_ZhbAvADQo")
    for user in User.objects.all():
        if user.profile.tg_notify_alerts and user.profile.tg_user_id:
            notifier.send_notification(chat_id=user.profile.tg_user_id,
                                       text=text)


if __name__ == '__main__':
    notify()
