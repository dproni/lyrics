# Scrapy settings for test_scrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
def setup_django_env(path):
    import imp
    from django.core.management import setup_environ

    f, filename, desc = imp.find_module('settings', [path])
    project = imp.load_module('settings', f, filename, desc)

    setup_environ(project)

setup_django_env('/home/marvin/lyrics/lyrics/')

ITEM_PIPELINES = [
    'test_scrapy.pipelines.LyricsPipeline',
    ]

BOT_NAME = 'test_scrapy'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['test_scrapy.spiders']
NEWSPIDER_MODULE = 'test_scrapy.spiders'
DEFAULT_ITEM_CLASS = 'test_scrapy.items.LyricsItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
DOWNLOAD_DELAY = 0.1
DOWNLOAD_TIMEOUT = 30
DEFAULT_RESPONSE_ENCODING = 'utf-8'