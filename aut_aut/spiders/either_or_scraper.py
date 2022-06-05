from scrapy.spiders import XMLFeedSpider


class EitherOrSpider(XMLFeedSpider):
    name = "either_or"
    allowed_domains = ['sks.dk']
    start_urls = [
        'http://www.sks.dk/EE1/txt.xml',
    ]
    itertag = 'lyn'

    def parse_node(self, response, node):
        self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.getall()))

        item = TestItem()
        return item
