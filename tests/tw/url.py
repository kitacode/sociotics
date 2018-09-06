import unittest
import asyncio
from src.tw.url import profile, reply


class TestUrl(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.new_event_loop()

    def test_profile(self):
        ### fake username & init
        username = "agnezmo"
        init = -1

        # run init = -1
        _url = self.loop.run_until_complete(profile(username, init))
        self.assertEqual(f"https://twitter.com/i/profiles/show/{username}/"
                         f"timeline/tweets?include_available_features=1&"
                         f"lang=en&include_entities=1&include_new_items_bar=true", _url)

        # run init != -1
        init = "test"
        _url = self.loop.run_until_complete(profile(username, init))
        self.assertEqual(f"https://twitter.com/i/profiles/show/{username}/"
                         f"timeline/tweets?include_available_features=1&"
                         f"lang=en&include_entities=1&include_new_items_bar=true&"
                         f"max_position={init}", _url)

    def test_reply(self):
        ### fake username & init & tweet_id
        username = "agnezmo"
        init = -1
        tweet_id = "1234567890"

        # run init = -1
        _url = self.loop.run_until_complete(reply(username, tweet_id, init))
        self.assertEqual(f"https://twitter.com/i/{username}/conversation/{tweet_id}?"
                         f"include_available_features=1&include_entities=1&"
                         f"max_position={init}&reset_error_state=false", _url)

        # run init != -1
        init = "test"
        _url = self.loop.run_until_complete(reply(username, tweet_id, init))
        self.assertEqual(f"https://twitter.com/i/{username}/conversation/{tweet_id}?"
                         f"include_available_features=1&include_entities=1&"
                         f"max_position={init}&reset_error_state=false", _url)
