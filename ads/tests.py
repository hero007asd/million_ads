from django.test import TestCase
from ads.models import Shop
import codecs
from million_ads.settings import BASE_DIR
from django.template.loader import render_to_string

# Create your tests here.
def create_html():
    results = Shop.objects.all()
    print results
    news_file = codecs.open('%s/ads/templates/template_index1.html' % BASE_DIR, 'wb', 'utf-8')
    try:
        html = render_to_string('template_index.html',{'shop_list':results})
        print news_file
        news_file.write(html)
    except IOError:
        print 'error'
    finally:
        news_file.close()
    print BASE_DIR

create_html()