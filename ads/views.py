from django.http import HttpResponse
from ads.models import Shop
from django.http.response import Http404
import json

def get_dp_detail(request):
    shop_id = ''
    results = []
    if 'p' in request.GET:
        shop_id = request.GET['p']
        if not shop_id:
            return HttpResponse('Enter a search term.')
        else:
#             qset = (
#                 Q()
#             )
            results = Shop.objects.filter(id=shop_id)
#             results =  getJson(results)
            a = {'shop_name':results[0].shop_name,
                 'web_site':results[0].web_site,
                 'info':results[0].info,
                 'logo_path':results[0].logo_path,
                 'join_time':str(results[0].join_time)}
            print json.dumps(a,separators=(',',':'))
            return HttpResponse(json.dumps(a,separators=(',',':')))
    else:return Http404
    

