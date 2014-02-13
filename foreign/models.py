from django.db import models, connection,transaction
from django.utils.html import format_html

# Create your models here.
class User(models.Model):
    login_name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=128)
    ini_money = models.IntegerField(blank=True,null=True)
    lever = models.IntegerField(blank=True,null=True)
    now_money = models.IntegerField(blank=True,null=True)
    
    def register(self):
        user=None
        # try:
        cursor = connection.cursor()
        cnt = cursor.execute('insert into foreign_user(login_name,pwd,ini_money,lever,now_money) values(%s,password(%s),%s,%s,%s)',
                       [self.login_name, self.pwd, self.ini_money, self.lever, self.now_money])
        print cnt
        if cnt != 0:
            user = User.objects.get(login_name=self.login_name)
#                 user = cursor.execute('select * from foreign_user where login_name = %s and pwd=password(%s)', [self.login_name, self.pwd])
        transaction.commit_unless_managed()
        cursor.close()
        connection.close()
        # except:
        #     return None
        return user
    def login(self):
        cursor = connection.cursor()
        user = cursor.execute('select * from foreign_user where login_name = %s and pwd=password(%s)', [self.login_name, self.pwd])
        cursor.close()
        connection.close()
        print user
    
    def __unicode__(self):#for admin's page show in order's management page
        return self.login_name
#     def __str__(self):
#         return 'login_name:%s,pwd:%s,ini_money:%d,lever:%d,now_money:%d' % (self.login_name, self.pwd, self.ini_money, self.lever, self.now_money)
    
class Order(models.Model):
    user = models.ForeignKey(User)
    balance = models.IntegerField()
    lots = models.DecimalField(max_digits=3, decimal_places=2,verbose_name='lots(0.1 etc)')
    currency_type = models.CharField(max_length=10,blank=True,null=True)
    start_pts = models.DecimalField(max_digits=9, decimal_places=5,blank=True,null=True)
    stop_profit_pts = models.DecimalField(max_digits=9, decimal_places=5,blank=True,null=True)
    stop_loss_pts = models.DecimalField(max_digits=9, decimal_places=5,blank=True,null=True)
    close_pts = models.DecimalField(max_digits=9, decimal_places=5,blank=True,null=True)
    start_time = models.DateTimeField(auto_now=True)
    close_time = models.DateTimeField(auto_now=True)
    profit = models.CharField(max_length=10,blank=True,null=True)
    def start_time_zh(self):
        return self.start_time.strftime('%Y-%m-%d %H:%M:%S')
    def orderProfit(self):
        return round((self.close_pts-self.start_pts)*10000*self.lots*10,2)
    def orderPts(self):
        return round((self.close_pts-self.start_pts)*10000,2)
    start_time_zh.short_description= 'chinese time'
    orderProfit.short_description = 'profit($)'
    orderPts.short_description = 'orderPts'

class CurrencyType(models.Model):
    type_name = models.CharField(max_length=10)
    deposit = models.DecimalField(max_digits=4, decimal_places=2)
    info = models.TextField()
    
class Person(models.Model):
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    birthday = models.DateField()
    is_active = models.BooleanField()
    slug = models.SlugField(max_length=40,unique=True, help_text='Unique value for product page URL, created from name.')

    def decade_born_in(self):
        return self.birthday.strftime('%Y')[:3]+'0\'s'
    decade_born_in.short_description = 'Brith decade'

    def born_in_fifities(self):
        return self.birthday.strftime('%Y')[:3] == '195'
    born_in_fifities.boolean = True

    # def colored_name(self):
    #     return format_html('<span style="color:red;">{1}</span>',self.nickname)
    # colored_name.allow_tags = True