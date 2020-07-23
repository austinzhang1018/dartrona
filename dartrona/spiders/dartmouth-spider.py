import scrapy
from newsplease import NewsPlease
from dartrona.items import ArticleItem

class CovidSpider(scrapy.Spider):
    name = "dartmouth"

    keywords = ['covid', 'covid-19', 'coronavirus', 'quarantine']

    allowed_domains = ['news.dartmouth.edu']
    start_urls = [
        "https://news.dartmouth.edu/covid-19/covid-19-coronavirus-information",
    ]

    def parse(self, response):
        try:
            article = NewsPlease.from_html(response.body, response.url)
            text = article.maintext
            if any(x in text.lower() for x in self.keywords):
                item = ArticleItem()
                item['title'] = article.title
                item['text'] = text
                item['url'] = response.url
                print('Saved', response.url)
                yield item
        except:
            pass

        # Get all the <a> tags
        a_selectors = response.xpath("//a")
        # print('SELECTORS', a_selectors)
        # Loop on each tag
        for selector in a_selectors:
            text = selector.xpath("text()").extract_first()
            link = selector.xpath("@href").extract_first()
            if link != None:
                if 'https://' not in link:
                    link = 'https://news.dartmouth.edu%s' % link
                # print(link)
                request = response.follow(link, callback=self.parse)
                # Return it thanks to a generator
                yield request
