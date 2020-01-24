import scrapy



class ExamSchedule(scrapy.Spider):
    name = "schedule_update"
    start_urls = [
        "https://www.ccs-labs.org/teaching/exams/",
    ]

    def parse(self, response):
        text = response.css('#footer-right').get()
        
        yield {
            'modified_date': text[62:-20],
        }
