from django.db import models


class Deal(models.Model):
    customer = models.CharField(max_length=200, verbose_name='Customer')
    item = models.CharField(max_length=200, verbose_name='Product')
    quantity = models.IntegerField(verbose_name='Quantity')
    price = models.IntegerField(verbose_name='Price')
    deal_date = models.DateTimeField(verbose_name='Deal Date')

    def __str__(self):
        return f'{self.customer} | {self.deal_date.strftime("%Y-%m-%d")}'

    class Meta:
        verbose_name_plural = 'Deals'
