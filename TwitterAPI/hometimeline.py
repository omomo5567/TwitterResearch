import key
import json

# ログイン認証
twitter = key.CreateOAuthSession()

#Endpoint
url = "https://api.twitter.com/1.1/statuses/home_timeline.json"

count = int(input("Get at once(max:180) >>"))    # 一度に取得するtweet数(Max=180)
params = {
    "count":count,        # 取得するツイート数
    "include_entities":True,    # 画像や動画を含むかどうか
    "exclude_replies":False,    # リプライ(返信)を含まないかどうか(Trueで含まない)
    "include_rts":True          # リツイートを含むかどうか
}
req = twitter.get(url, params = params)

print('----------------------------------------------------')

if req.status_code == 200:
    timeline = json.loads(req.text)
    for tweet in timeline:
        print(tweet['user']['name']+'::'+tweet['text'])
        print(tweet['created_at'])
        print('----------------------------------------------------')
else:
    print("ERROR: %d" % req.status_code)
