# Signalisation Crawler

Réinitialisation de la mongodb signs avant lancement du crawler

```bash
$ sudo service mongod start 
$ cd var/lib/mongodb
/var/lib/mongodb$ mongo --host 127.0.0.1:27017
> use db passeTonCode
> db.dropDatabase()
```

Lancement du crawler via Scrapy

```bash
ptc-crawler$ scrapy crawl signs
```

Liens utiles

* [Scrapy](https://doc.scrapy.org/en/latest/)
* [tutorial](https://realpython.com/blog/python/web-scraping-with-scrapy-and-mongodb/)
