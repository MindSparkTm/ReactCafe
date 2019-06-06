from django.db import models
from djmoney.models.fields import MoneyField
from currencies.models import Currency
from django.shortcuts import reverse
from dj.choices import Choices, Choice
from dj.choices.fields import ChoiceField
import  logging
# Create your models here.

class MenuType(Choices):
    Side = Choice("side")
    MainCourse = Choice("maincourse")
    Appetizer = Choice("appetizer")
    Dessert = Choice('dessert')
    NotSpecified = Choice('not specified')

def set_default_currency():
    try:
        currency = Currency(code='USD',name='US Dollar',symbol='$')
    except Exception as e:
        logging.debug('Exception occured in creating default currency',str(e))
    else:
        currency.save()

class Menu(models.Model):
    name = models.CharField(max_length=100)
    currency = models.ForeignKey(Currency,on_delete=models.PROTECT,default=set_default_currency(),
                                 null=True,blank=True)
    price = models.DecimalField(max_digits=19,decimal_places=2)
    type = ChoiceField(choices=MenuType,default=MenuType.NotSpecified)
    image = models.ImageField(null=True, blank=True,default='image_avail.png')
    date_last_modified = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural='Menu'
        verbose_name='Menu'

    def __str__(self):
        return '{}{}'.format(self.name,self.price)

    def save(self,*args,**kwargs):
        if self.pk is None:
            if self.currency is None:
                currency = Currency.objects.get(code='USD')
                self.currency = currency
        super(Menu, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('menu-details', args=[str(self.id)])



