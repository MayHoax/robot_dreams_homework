class Bot:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)

    def send_message(self, message):
        print(message)


class TelegramBot(Bot):
    def __init__(self, name, url=None, chat_id=None):
        super().__init__(name)
        self.url = url
        self.chat_id = chat_id

    def send_message(self, message):
        print(f'Telegram Bot says "{message}", to chat {self.chat_id} using {self.url} '
            )

    def set_url(self, url):
        self.url = url

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id


class MyStr(str):
    def __str__(self):
        return self.upper()


class User():
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, User):
            return self.name.lower() == other.name.lower()
        return False

