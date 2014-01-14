from django.shortcuts import render, render_to_response
from foreign import models
from django.http.response import HttpResponseRedirect
from django.template.context import RequestContext

# Create your views here.
def inimoney(request):
    if request.method == 'POST':
        user = models.User()
        if 'loginId' in request.POST:
            user.login_name = request.POST['loginId']
            if not user.login_name:
                return render_to_response('foreign.html', context_instance=RequestContext(request))
        if 'password' in request.POST:
            user.pwd = request.POST['password']
            if not user.pwd:
                return render_to_response('foreign.html', context_instance=RequestContext(request))
        if 'ini_money' in request.POST:
            user.ini_money = request.POST['ini_money']
            user.now_money = request.POST['ini_money']
        if 'lever' in request.POST:
            user.lever = request.POST['lever']
        user = user.register()
        print 'count:%s' % user
        if user is None:
            return render_to_response('foreign.html', context_instance=RequestContext(request))
        return render_to_response('my_foreign_log.html', {'user':user},context_instance=RequestContext(request))
#     param = ['loginId', 'password', 'ini_money', 'lever']
#     pa = {}
#     for p in param:
#         if p in request.POST:
#             pa[p] = request.POST[p]
#     user = models.User()
#     user.login_name = pa['loginId']
#     user.pwd = pa['password']
#     user.ini_money = pa['ini_money']
#     user.lever = pa['lever']
#     user.now_money = pa['ini_money']
#     count = user.register()
    return render_to_response('foreign.html', context_instance=RequestContext(request))

def login(request):
    if request.method == 'POST':
        user = []
        loginId = ''
        pwd = ''
        if 'loginId' in request.POST:
            loginId = request.POST['loginId']
            if not loginId:
                return render_to_response('login.html', context_instance=RequestContext(request))
        if 'password' in request.POST:
            pwd = request.POST['password']
            if not pwd:
                return render_to_response('login.html', context_instance=RequestContext(request))
        user = models.User.objects.filter(login_name=loginId, pwd=pwd)
        if not user.exists():
            return render_to_response('login.html', context_instance=RequestContext(request))
        return render_to_response('my_foreign_log.html', {'user':user[0],}, context_instance=RequestContext(request))
    return render_to_response('login.html', context_instance=RequestContext(request))

def saveOrder(request):
    if request.method == 'POST':
        order = models.Order()
        if 'username' in request.POST:
            userId = int(request.POST['username'])
            print userId
            order.user = models.User.objects.get(id=userId)
        if 'balance' in request.POST:
            order.balance = request.POST['balance']
        if 'lots' in request.POST:
            order.lots = request.POST['lots']
        if 'currency_type' in request.POST:
            order.currency_type = request.POST['currency_type']
        if 'start_point' in request.POST:
            order.start_pts = request.POST['start_point']
        if 'stop_profit_point' in request.POST:
            order.stop_profit_pts = request.POST['stop_profit_point']
        if 'stop_loss_point' in request.POST:
            order.stop_loss_pts = request.POST['stop_loss_point']
        order.save()
        order = models.Order.objects.filter(user_id=order.user_id)
        return render_to_response('my_foreign_log.html',{'order':order,'user':order[0].user}, context_instance=RequestContext(request))
    return render_to_response()
