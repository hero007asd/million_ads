from django.contrib import admin
from django import forms
from foreign import models
from datetime import date
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

# class OrderForm(forms.ModelForm):
# 	class Meta:
# 		model = models.Order
class OrderAdmin(admin.ModelAdmin):
	list_display = ('user','balance','lots','start_pts','close_pts','start_time','orderProfit','orderPts','uppser_case_name')
	search_fields = ('user',)	
	# list_filter = ('start_time','lots','user__ini_money')
	list_filter = ('start_time','lots',)
	date_hierarchy = 'start_time'
	ordering = ('-start_time','lots')
	# fields = ('user','start_pts','lots','balance')
	# filter_horizontal&filter_vertical; for many 2 many keys
	raw_id_fields = ('user',)
	fieldsets=(
		(None,{
			'fields':('user','start_pts','lots','balance')
			}),
	    ('Advanced options',{
	    	# 'classes':('extrapretty','wide'),
	    	'description':'advanced options test',
	    	'classes':('collapse','wide'),
	    	'fields':('currency_type',('stop_profit_pts','stop_loss_pts'),'close_pts')#,'close_time','profit')
	    	}),
	)
	# formfield_overrides = {
	# 	models.TextField: {'widget':RichTextEditorWidget},
	# }
	# exclude = ['close_pts']
	# form = OrderForm

	def uppser_case_name(self,obj):
		return ('%s' % obj.currency_type).upper()
	uppser_case_name.short_description = 'CurrencyType1'


# class TypeAdmin(admin.ModelAdmin):
# 	formfield_overrides={
# 		models.TextField:{'widget':RichTextEditorWidget},
# 	}

class DecadeBornListFilter(admin.SimpleListFilter):
	title = _('decade born')
	parameter_name='decade'
	def lookups(self,request,model_admin):
		return (
			('80',_('in the eighties')),
			('90',_('in the nineties')),
			)
	def queryset(self,request,queryset):
		if self.value() == '80s':
			return queryset.filter(birthday__gte=date(1980,1,1),birthday__lte=date(1989,12,31))
		if self.value() == '90s':
			return queryset.filter(birthday__gte=date(1990,1,1),birthday__lte=date(1999,12,31))

class PersonAdmin(admin.ModelAdmin):
	list_display = ('name','decade_born_in','is_active','born_in_fifities')
	list_display_links = ('name','decade_born_in')
	list_filter = (DecadeBornListFilter,)
	list_per_page = 10
	prepopulated_fields = {'slug':('name',)}
	readonly_fields = ('address_report',)
	def address_report(self,instance):
		return format_html_join(mark_safe('<br/>'), '{0}', ((line,) for line in instance.name), ) or '<span class="errors">i can\'t determine this address.</span>'
		# return format_html_join(mark_safe('<br/>'), '{0}', ((line,) for line in instance.birthday), ) or '<span class="errors">i can\'t determine this address.</span>'
	address_report.short_description = 'address'
	address_report.allow_tags = True
	#TODO
	# README
	#list_max_show_all = 20
	#list_select_related = ('person','blog')
	#IS_OK
	# list_editable = ('is_active',)
# Register your models here.
admin.site.register(models.UserTemp)
# admin.site.register(models.Order)
admin.site.register(models.Order,OrderAdmin)
admin.site.register(models.CurrencyType)
admin.site.register(models.Person,PersonAdmin)