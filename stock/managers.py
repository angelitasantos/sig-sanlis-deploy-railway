from django.db import models


class StockSaleManager(models.Manager):

    def get_queryset(self):
        return super(StockSaleManager, self).get_queryset().filter(tipo_movimento='V')


class StockServiceManager(models.Manager):

    def get_queryset(self):
        return super(StockServiceManager, self).get_queryset().filter(tipo_movimento='S')


class StockShoppingManager(models.Manager):

    def get_queryset(self):
        return super(StockShoppingManager, self).get_queryset().filter(tipo_movimento='C')


class StockProductionManager(models.Manager):

    def get_queryset(self):
        return super(StockProductionManager, self).get_queryset().filter(tipo_movimento='P')


class StockInventaryManager(models.Manager):

    def get_queryset(self):
        return super(StockInventaryManager, self).get_queryset().filter(tipo_movimento='I')
