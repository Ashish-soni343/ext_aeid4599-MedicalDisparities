# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MedicareDisparitiesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # Source = scrapy.Field()
    primary_denominator = scrapy.Field()
    Analysis_value = scrapy.Field()
    Adustment = scrapy.Field()
    Race_and_Ethnicity = scrapy.Field()
    Medicare_Eligibility = scrapy.Field()
    Dual_Eligible = scrapy.Field()
    Year = scrapy.Field()
    state = scrapy.Field()
    Geography = scrapy.Field()
    Fips = scrapy.Field()
    county = scrapy.Field()
    urban = scrapy.Field()
    Measure = scrapy.Field()
    Condition_Service = scrapy.Field()
    #Condition = scrapy.Field()
    #len = scrapy.Field()
    Sex = scrapy.Field()
    Age = scrapy.Field()
    Feed_code = scrapy.Field()
    Site = scrapy.Field()
    Source_country = scrapy.Field()
    Record_create_by = scrapy.Field()
    Execution_id = scrapy.Field()
    # item["Execution_id"] = self.execution_id
    Record_create_dt = scrapy.Field()
    file_create_dt = scrapy.Field()
    #br = scrapy.Field()
    pass
