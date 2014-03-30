import math
def factorial(n):
    return math.factorial(n)
#n*0.667*10+n*0.667*9


def my_decorate(func):
    print 'oops starting'
    # func
    print 'oops bye'
    return func

def my_dec(args):
	print 'first'
	def myfun(func):
		print 'args:'+args
		return func
	return myfun
def timeit(func):
	import time
	import functools
	@functools.wraps(func)
	def wrapper(a,b,c):
		start = time.clock()
		func(a,b,c)
		end = time.clock()
		print '[%s] used time:%s s' % (func.__name__.title(),end - start)
	return wrapper

@timeit	
@my_dec('as')	
@my_decorate
def captical_and_profit(ini_money,rate,years):
	all_year = sum(range(years))
	for i in range(years+1):
		print ini_money*i + ini_money*rate*sum(range(i))
	print 'benjin:',ini_money*years
	return ini_money*rate*all_year+ini_money*years



captical_and_profit(70000, 0.0667, 5)
print captical_and_profit.__name__


# ===============mako test==========================
from mako.template import Template
mytemplate = Template('hello,${name}!')
print mytemplate.render(name='sand')
