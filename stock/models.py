from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy
from home.models import TimeStampedModel
from activation.models import Company
from plataform.models import Partner, Item
from .managers import   (
                            StockSaleManager, 
                            StockServiceManager,
                            StockShoppingManager,
                            StockProductionManager,
                            StockInventaryManager
                        )


MOVIMENTO = (
    ('E', 'entrada'),
    ('S', 'saida'),
)

TIPO_MOVIMENTO = (
    ('V', 'VENDA'),
    ('S', 'SERVIÇO'),
    ('C', 'COMPRA'),
    ('P', 'PRODUÇÃO'),
    ('I', 'INVENTÁRIO'),
)


class Estoque(TimeStampedModel):
    choices_tipo_registro = (   ('1', 'Não Autorizado'),
                                ('2', 'Pedido'),
                                ('3', 'Troca'),
                                ('4', 'Devolução'),
                                ('5', 'Garantia'),
                                ('6', 'Consignado'))
    choices_status = (  ('1', 'Não Iniciado'),
                        ('2', 'Em Aberto'),
                        ('3', 'Finalizado'))
    tipo_registro = models.CharField(max_length=1, choices=choices_tipo_registro, default="2")
    status = models.CharField(max_length=1, choices=choices_status, default="2")

    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    nf = models.PositiveIntegerField('nota fiscal', null=True, blank=True)
    movimento = models.CharField(max_length=1, choices=MOVIMENTO, blank=True)
    tipo_movimento = models.CharField(max_length=1, choices=TIPO_MOVIMENTO, blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        if self.nf:
            return '{} - {} - {}'.format(self.pk, self.nf, self.created.strftime('%d-%m-%Y'))
        return '{} --- {}'.format(self.pk, self.created.strftime('%d-%m-%Y'))
    
    def nf_formated(self):
        if self.nf:
            return str(self.nf).zfill(3)
        return '---'


class StockSale(Estoque):

    objects = StockSaleManager()

    class Meta:
        proxy = True
        verbose_name = 'registro de venda'
        verbose_name_plural = 'registros de vendas'
    
    def get_absolute_url(self):
        return reverse_lazy('stock:stock_sale_detail', kwargs={'pk': self.pk})


class StockService(Estoque):

    objects = StockServiceManager()

    class Meta:
        proxy = True
        verbose_name = 'registro de serviço'
        verbose_name_plural = 'registros de serviços'

    def get_absolute_url(self):
        return reverse_lazy('stock:stock_service_detail', kwargs={'pk': self.pk})


class StockShopping(Estoque):

    objects = StockShoppingManager()

    class Meta:
        proxy = True
        verbose_name = 'registro de compra'
        verbose_name_plural = 'registros de compras'

    def get_absolute_url(self):
        return reverse_lazy('stock:stock_shopping_detail', kwargs={'pk': self.pk})


class StockProduction(Estoque):

    objects = StockProductionManager()

    class Meta:
        proxy = True
        verbose_name = 'registro de produção'
        verbose_name_plural = 'registros de produção'

    def get_absolute_url(self):
        return reverse_lazy('stock:stock_production_detail', kwargs={'pk': self.pk})


class StockInventary(Estoque):

    objects = StockInventaryManager()

    class Meta:
        proxy = True
        verbose_name = 'registro de inventário'
        verbose_name_plural = 'registros de inventário'

    def get_absolute_url(self):
        return reverse_lazy('stock:stock_inventary_detail', kwargs={'pk': self.pk})


class EstoqueItens(models.Model):
    estoque = models.ForeignKey(
        Estoque,
        on_delete=models.CASCADE,
        related_name='estoques'
    )
    produto = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField()

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.estoque.pk, self.produto)
