from asyncio import get_event_loop
from json import loads
from bs4 import BeautifulSoup
from tw import url
from tw.get import Request
from tw.tweet import tweets


class TwitterTweetTimeline:
    def __init__(self):
        self.username = 'PartaiHulk'
        self.init = -1
        self.is_run = True
        self.count = 0
        self.timeline = []

    async def main(self):
        while self.is_run:
            _url = await url.profile(self.username, self.init)
            response = await Request(_url)
            try:
                feed, self.init = self.extract(response)
                for tweet in feed:
                    self.count += 1
                    t = await tweets(tweet, None, self.username)
                    if t:
                        self.timeline.append(t)
            except:
                self.is_run = False

    @staticmethod
    def extract(response):
        json_response = loads(response)
        html = json_response["items_html"]
        soup = BeautifulSoup(html, "html.parser")
        feed = soup.find_all("li", "js-stream-item")
        return feed, feed[-1]["data-item-id"]

    def get_data(self):
        return self.timeline

    def run(self):
        get_event_loop().run_until_complete(self.main())


if __name__ == '__main__':
    ttt = TwitterTweetTimeline()
    ttt.run()
    for t in ttt.get_data():
        print(t)
