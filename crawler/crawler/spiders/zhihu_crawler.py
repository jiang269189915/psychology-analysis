import scrapy


class ZhihuSpider(scrapy.Spider):
    name = "zhihu"
    start_urls = [
        "https://www.zhihu.com"
    ]
    def login(self):
        return [scrapy.FormRequest("http://www.zhihu.com/login/phone_num",
                                   formdata={"phone_num":"15800679781", "password":"jiangweiwei5310",
                                             "_xsrf":"a62d4a923e1156d3ebdfd2779422010d",
                                             "captcha_type":"cn"},
                                   callback=self.login)]

    def parse(self, response):
        print response.text()
