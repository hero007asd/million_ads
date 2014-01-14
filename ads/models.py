from django.db import models
from json.encoder import JSONEncoder
from django.db.models.query import QuerySet
from django.core.serializers import serialize
from json import loads
import json

class Shop(models.Model):
#     shop_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=50)
    web_site = models.CharField(max_length=200)
    logo_path = models.CharField(max_length=200)
    info = models.CharField(max_length=500)
    join_time = models.DateTimeField(auto_now=True, auto_now_add=True)
    location = models.CharField(max_length=40)
    price = models.CharField(max_length=10)
    def __str__(self):
        return '%s %s' % (self.shop_name, self.web_site)
    def __unicode__(self):
        return u'%s' % (self.shop_name)
    
class LookLog(models.Model):
#     log_id = models.AutoField(primary_key=True)
    shop = models.ForeignKey(Shop)
    log_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s' % (self.shop)
    def __unicode__(self):
        return self.shop
    
    
# class PingJa:
# 
# class member:


#=========================deal with json for model================================================
class DjangoJSONEncoder(JSONEncoder):
    def default(self,obj):
        if isinstance(obj, QuerySet):
            # `default` must return a python serializable
            # structure, the easiest way is to load the JSON
            # string produced by `serialize` and return it
            return loads(serialize('json',obj))
        return JSONEncoder.default(self,obj)

def getJson(obj):   
    return json.dumps(obj,cls=DjangoJSONEncoder)
    