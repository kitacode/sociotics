from asyncio import get_event_loop
from twint.get import Request
from twint.user import User
from bs4 import BeautifulSoup


class TwitterUsers:
    def __init__(self):
        self.loop = get_event_loop()

    def get_profile(self, username):
        url = f"http://twitter.com/{username}?lang=en"
        response = self.loop.run_until_complete(Request(url))
        u = BeautifulSoup(response, "html.parser")
        return User(u).__dict__


if __name__ == '__main__':
    tw_usr = TwitterUsers()
    print(tw_usr.get_profile('agnezmo'))
