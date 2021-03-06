from pymongo import MongoClient

def mongo(post):
    client = MongoClient('localhost', 27017)
    db = client.testDB
    collection = db.test_collection

    """
    # 登録データ作成
    post = {"author": "山田太郎",
            "text": "pymongoテスト",
            "tags": ["mongodb", "python", "pymongo"]}
    """

    # 登録
    post_id = collection.insert_one(post).inserted_id
    # 閉じる
    client.close()

    return post_id
