import math
def factorial(n):
    return math.factorial(n)
#n*0.667*10+n*0.667*9
def captical_and_profit(ini_money,rate,years):
	all_year = sum(range(years))
	for i in range(years+1):
		print ini_money*i + ini_money*rate*sum(range(i))
	print 'benjin:',ini_money*years
	return ini_money*rate*all_year+ini_money*years

print captical_and_profit(70000, 0.0667, 5)

