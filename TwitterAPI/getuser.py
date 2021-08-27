import key
import json

#ログイン認証
twitter = key.CreateOAuthSession()

#Endpoint
url = "https://api.twitter.com/1.1/users/show.json"

name = input("type id >>")

#Enedpointへ渡すパラメーター
params = {
    "screen_name":name,
    "include_entities":True, #画像などを含めるか、trueなら含める
}

req = twitter.get(url, params = params)

if req.status_code == 200:  #成功した時にuser情報を表示
    user=json.loads(req.text)
    print(user)

else:
    print("ERROR: %d" % req.status_code)
