# lihkg_collector
get articles (json) from lihkg

![alt text](https://i.imgur.com/uDyofga.png)

## Lihkg
#### article_collector
* 以 `forum_code` 為參數爬取 Lihkg(連登論壇) 特定台的文章。論壇編號請參考 lihkg 分類。

* 以 `sort_by` 為參數爬取最新 (`new`) 或熱門 (`hot`) 文章。
* 回傳值為 list。list 內含數個 dict，主要有：  
    1,`thread_id`(文章 ID)  
    2,`title`(文章標題)  
    3,`user_nickname`(作者暱稱)  
    4,`like_count`(按讚數)  
    5,`total_page`(總頁數)  
    6,`category`(文章分類(dict))  
    等...

## Requirements
python 3

## Usage
```
if __name__ == "__main__":
    lihkg = Lihkg()
    all_articles = lihkg.article_collector("1", "new")
```

## Installation
`pip install -r requriements.txt`

