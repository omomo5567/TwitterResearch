
import json
import key

# ログイン認証
twitter = key.CreateOAuthSession()

# Twitter Endpoint(検索結果を取得する)
url = 'https://api.twitter.com/1.1/tweets/search/fullarchive/test.json' #envname間違えないこと。Fullアーカイブはtest

#Enedpointへ渡すパラメーター
params ={
         'query' : "from:omomo5567" ,  # 検索キーワード ,
         'maxResults': 100 ,   # 取得するtweet数
        }

req = twitter.get(url, params = params)

if req.status_code == 200:
    res = json.loads(req.text)
    for line in res['results']:
        print(line['text'])
        print('----------------------------------------------------')
else:
    print("Failed: %d" % req.status_code)
