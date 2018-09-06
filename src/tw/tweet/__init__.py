import re


async def tweets(tw, location, username):
    copyright = tw.find("div", "StreamItemContent--withheld")
    if copyright is None and is_tweet(tw):
        t = Tweet()
        t.id = tw.find("div")["data-item-id"]
        t.datetime = int(tw.find("span", "_timestamp")["data-time"])
        t.user_id = tw.find(
            "a", "account-group js-account-group js-action-profile js-user-profile-link js-nav")["data-user-id"]
        t.username = tw.find("span", "username").text.replace("@", "")
        for img in tw.findAll("img", "Emoji Emoji--forText"):
            img.replaceWith(img["alt"])
        t.location = location
        t.link = f"https://twitter.com/{t.username}/status/{t.id}"
        t.mentions = getMentions(tw)
        t.tweet = getTweet(tw, t.mentions)
        t.hashtags = getHashtags(t.tweet)
        t.replies = getStat(tw, "reply")
        t.retweets = getStat(tw, "retweet")
        t.likes = getStat(tw, "favorite")
        t.retweet = getRetweet(True, t.username, username)
        t.user_rt = getUser_rt(True, t.username, username)

        # t.datestamp = strftime("%Y-%m-%d", localtime(t.datetime))
        # t.timestamp = strftime("%H:%M:%S", localtime(t.datetime))
        # t.timezone = strftime("%Z", localtime())

        return t.__dict__


def is_tweet(tw):
    try:
        tw.find("div")["data-item-id"]
        return True
    except:
        return False


class Tweet:
    def __init__(self):
        pass


def getMentions(tw):
    try:
        mentions = tw.find("div", "js-original-tweet")["data-mentions"].split(" ")
    except:
        mentions = ""

    return mentions


def getTweet(tw, mentions):
    try:
        text = getText(tw)
        for i in range(len(mentions)):
            mention = f"@{mentions[i]}"
            if mention not in text:
                text = f"{mention} {text}"
    except:
        text = getText(tw)

    return text


def getText(tw):
    text = tw.find("p", "tweet-text").text
    text = text.replace("\n", "")
    text = text.replace("http", " http")
    text = text.replace("pic.twitter", " pic.twitter")

    return text


def getHashtags(text):
    return re.findall(r'(?i)\#\w+', text, flags=re.UNICODE)


def getStat(tw, _type):
    st = f"ProfileTweet-action--{_type} u-hiddenVisually"
    return tw.find("span", st).find("span")["data-tweet-stat-count"]


def getRetweet(profile, username, user):
    if not user:
        return False
    if profile and username.lower() != user.lower():
        return True
    return False


def getUser_rt(profile, username, user):
    if getRetweet(profile, username, user):
        user_rt = user
    else:
        user_rt = "None"

    return user_rt
