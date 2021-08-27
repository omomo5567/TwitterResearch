import key
import json
import sys
sys.path.append('..')
import mongo

#ログイン認証
twitter = key.CreateOAuthSession()

#Endpoint
url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

name = input("type id >>")
count = int(input("Get at once(max:180) >>"))
#Enedpointへ渡すパラメーター
params = {
    "screen_name":name,         # ユーザーID
    "count":count,              # 表示数
    "include_entities":True,    # 画像などを含めるか、trueなら含める
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

mongo_id=mongo.mongo(req)
