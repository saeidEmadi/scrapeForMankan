import scrapy


class MankanSpider(scrapy.Spider):
    name = "mankan"
    
    def start_requests(self):
        MAX_PRODUCTS = 10
        for index in range(MAX_PRODUCTS):
            yield scrapy.Request(url = f"https://mankan.me/mag/lib/read_one.php?id={index}", \
                                 callback = self.detailer, meta = {'index' : index})

    def detailer(self, response):
        yield {'siteId' : response.meta['index'],
               'name' : response.css("div.read-one-header h1 ::text").get(),
               'calory' : response.css("div.calory-box span#calory-amount ::text").get(),
               'carbo' : response.css("div.carbo-box span#carbo-amount ::text").get(),
               'protein' :  response.css("div.protein-box span#protein-amount ::text").get(),
               'fat' : response.css("div.fat-box span#fat-amount ::text").get(),
               'fiber' : response.css("div.fiber-box span#fiber-amount ::text").get(),
               'activity1' : response.css("div.icon-activity p#number-activity-1 ::text").get(),
               'activity2' : response.css("div.icon-activity p#number-activity-2 ::text").get(),
               'activity3' : response.css("div.icon-activity p#number-activity-3 ::text").get(),
               'activity4' : response.css("div.icon-activity p#number-activity-4 ::text").get()
        }