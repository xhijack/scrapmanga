# scrapmanga

this script for scraping manga from http://www.mangagebo.com/ using scrapy framework

# How to use
- setup your environment
- running on your console

```sh
git pull origin https://github.com/xhijack/scrapmanga
cd scrapmanga
pip install -r requirement.text
```

```
#settings.py
FILES_STORE = ''
IMAGES_STORE = '
```

- Setting path in scrapmangaku.settings
```sh
scrapy crawl manga -a manga_url=http://www.mangagebo.com/fairy-tail/
```
### Todos

 - Write Tests
