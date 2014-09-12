from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from example.items import ExampleItem

class MySpider(BaseSpider):
    name = "njit"
    allowed_domains=["catalog.njit.edu"]
    start_urls = ["http://catalog.njit.edu/courses/cs.php#gradcourses","http://catalog.njit.edu/courses/acct.php#gradcourses","http://catalog.njit.edu/courses/arch.php#gradcourses","http://catalog.njit.edu/courses/bnfo.php#gradcourses","http://catalog.njit.edu/courses/biol.php#gradcourses",
    "http://catalog.njit.edu/courses/bme.php#gradcourses","http://catalog.njit.edu/courses/bio.php#gradcourses","http://catalog.njit.edu/courses/che.php#gradcourses"]
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("//p")
        items = []
        for titles in titles:
            item = ExampleItem()
            item['year'] = titles.select("span/text()").extract()[0]
            item['title']  = titles.select("a/b/text()").extract()[0]
            yield item