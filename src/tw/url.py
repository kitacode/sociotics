mobile = "https://mobile.twitter.com"
base = "https://twitter.com/i"


async def reply(username, tweet_id, init):
    url = f"{base}/{username}/conversation/{tweet_id}?"
    url += f"include_available_features=1&include_entities=1&"
    url += f"max_position={init}&reset_error_state=false"

    return url


async def profile(username, init):
    url = f"{base}/profiles/show/{username}/timeline/tweets?include_"
    url += "available_features=1&lang=en&include_entities=1"
    url += "&include_new_items_bar=true"

    if init != -1:
        url += f"&max_position={init}"

    return url
