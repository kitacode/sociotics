from store import Store
from datetime import datetime


class TwitterStoreUsers(Store):
    def __init__(self):
        super().__init__()

    def update_daily_stat(self, profile):
        pubdate = datetime.now().strftime('%Y%m%d')
        _id = "{}|{}".format(profile['id'], pubdate)

        stat = {
            '_id': _id,
            'pubdate': int(pubdate),
            'user_id': profile['id'],
            'followers': int(profile['followers']),
            'following': int(profile['following']),
            'likes': int(profile['likes']),
            'media': int(profile['media_count'].replace(",", "")),
        }

        coll = self.db['user_daily_stat']
        coll.update_one({'_id': _id}, {"$set": stat}, True)

        return self.get_daily_stat(_id)

    def get_daily_stat(self, _id):
        coll = self.db['user_daily_stat']
        return coll.find_one({'_id': _id})

