# Scrapy settings for NasaScraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'NasaScraper'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['NasaScraper.spiders']
NEWSPIDER_MODULE = 'NasaScraper.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = ['NasaScraper.pipelines.NasascraperPipeline', ]

MONGODB_SERVER = "192.168.101.5"
MONGODB_PORT = 27017
MONGODB_DB = "nasadb"
MONGODB_COLLECTION = "nasacollection"
