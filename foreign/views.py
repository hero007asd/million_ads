from django.shortcuts import render, render_to_response,redirect
from foreign import models
from django.http.response import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
# Create your views here.
@login_required(login_url='/foreign/login/')
def inimoney(request):
    # if request.method == 'POST':
    user = request.session['_auth_user_id']
    # if 'ini_money' in request.POST:
    #     user.ini_money = request.POST['ini_money']
    #     user.now_money = request.POST['ini_money']
    # if 'lever' in request.POST:
    #     user.lever = request.POST['lever']

    # user = user.register()
    # print 'count:%s' % user
    # if user is None:
    #     return render_to_response('foreign/foreign.html', context_instance=RequestContext(request))
    print 'user:',user,',:',request.user
    return render_to_response('foreign/my_foreign_log.html', {'user':user},context_instance=RequestContext(request))
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
    # return render_to_response('foreign/foreign.html', context_instance=RequestContext(request))

def mylogin(request):
    if request.method == 'POST':
        loginId = ''
        pwd = ''
        if 'loginId' in request.POST:
            loginId = request.POST['loginId']
            if not loginId:
                return render_to_response('foreign/login.html', context_instance=RequestContext(request))
        if 'password' in request.POST:
            pwd = request.POST['password']
            if not pwd:
                return render_to_response('foreign/login.html', context_instance=RequestContext(request))
        # user = models.User.objects.filter(login_name=loginId, pwd=pwd)
        user = authenticate(username=loginId,password=pwd)
        print user
        if user is None:
            return render_to_response('foreign/login.html', context_instance=RequestContext(request))
        login(request,user)
        # return render_to_response('foreign/my_foreign_log.html', {'user':user,}, context_instance=RequestContext(request))

        # return redirect('/foreign/index/')
        return redirect(reverse('foreign:index'))
    return render_to_response('foreign/login.html', context_instance=RequestContext(request))

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
        return render_to_response('foreign/my_foreign_log.html',{'order':order,'user':order[0].user}, context_instance=RequestContext(request))
    return render_to_response()
