import json
import requests

class Lihkg():
    def __init__(self):
        self.headers = {"referer": "https://lihkg.com/category/1?order=hot"}    
        self.api = "https://lihkg.com/api_v2/thread/"

    def article_collector(self, forum_code, sort_by):
        output = []
        page = 1
        if forum_code == "1":
            url = f"{self.api}latest?cat_id={forum_code}"
        else:
            url = f"{self.api}category?cat_id={forum_code}"
        while True:
            complete_url = url + f"&page={page}&count=100&type=now&order={sort_by}"
            text = requests.get(complete_url, headers=headers).text
            forum_articles = json.loads(text)
            if forum_articles["success"] == 1:
                output += forum_articles["response"]["items"]
                page+=1
            else:
                break
        return output


if __name__ == "__main__":
    lihkg = Lihkg()
    all_articles = lihkg.article_collector("1", "new")