from asyncio import get_event_loop
from tw.get import Request
from tw.tweet import tweets
from tw import url
from json import loads
from bs4 import BeautifulSoup


class TwitterTweetReply:
    def __init__(self):
        self.init = -1
        self.count = 0
        self.is_run = True
        self.username = None
        self.tweet_id = None
        self.reply = []

    def reset(self):
        self.init = -1
        self.count = 0
        self.is_run = True
        self.username = None
        self.tweet_id = None
        self.reply = []

    async def main(self):
        while self.is_run:
            _url = await url.reply(self.username, self.tweet_id, self.init)
            response = await Request(_url)

            feed = []
            try:
                feed, self.init = self.extract(response)
            except:
                pass

            if self.init is None:
                self.is_run = False

            for tweet in feed:
                self.count += 1
                t = await tweets(tweet, None, None)
                if t:
                    self.reply.append(t)

    @staticmethod
    def extract(response):
        json_response = loads(response)
        html = json_response["items_html"]
        soup = BeautifulSoup(html, "html.parser")
        feed = soup.find_all("li", "js-stream-item")
        return feed, json_response["min_position"]

    def get_data(self):
        return self.reply

    def run(self, username, tweet_id):
        self.reset()
        self.username = username
        self.tweet_id = tweet_id

        get_event_loop().run_until_complete(self.main())


if __name__ == '__main__':
    ttr = TwitterTweetReply()
    ttr.run("PartaiHulk", "972118443892785154")
    for t in ttr.get_data():
        print(t)
