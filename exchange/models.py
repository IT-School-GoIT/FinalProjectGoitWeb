from django.db import models


# Create your models here.
class Currencies(models.Model):
    bank_name = models.CharField(max_length=100)
    buy_eur = models.CharField()
    sell_eur = models.CharField()
    buy_usd = models.CharField()
    sell_usd = models.CharField()
    pln_buy = models.CharField()
    pln_sell = models.CharField()
    url_link = models.URLField()

    def __str__(self):
        return self.bank_name
