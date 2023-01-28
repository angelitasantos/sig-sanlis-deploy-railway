from django.shortcuts import render, redirect, resolve_url
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from activation.models import TokenUser, Company
from plataform.models import Item, Partner
from .models import (   
                        Estoque,
                        StockSale, 
                        StockService,
                        StockShopping,
                        StockProduction,
                        StockInventary,
                        EstoqueItens
                    )
from .forms import EstoqueForm, EstoqueItensEntradaForm, EstoqueItensSaidaForm


sig = 'SIG SANLIS | '
registers_for_page = 10


#######################################################
@login_required(login_url='/auth/login/')
def stock_list(request, template_name, objects, url, title, subtitle):
    objects = objects
    context =   {
                    'title': title,
                    'subtitle': subtitle,
                    'object_list': objects
                }
    return render(request, template_name, context)
    

@login_required(login_url='/auth/login/')
def stock_sale_list(request):
    title = sig + 'Vendas'
    subtitle = 'Vendas'
    template_name = 'stock_list.html'

    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    company_id = user_token_company[0]['company_id']
    
    objects = StockSale.objects.filter(company_id=company_id)
    objects_paginator = Paginator(objects, registers_for_page)
    page_number = request.GET.get('page')
    page = objects_paginator.get_page(page_number)
    url_page = 'stock:stock_sale_list'
    
    context =   {
                    'title': title,
                    'subtitle': subtitle,
                    'user_login': request.user,
                    'url_add': 'stock:stock_sale_add',
                    'object_list': objects,
                    'page': page,
                    'url_page': url_page
                }
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def stock_service_list(request):
    title = sig + 'Serviços'
    subtitle = 'Serviços'
    template_name = 'stock_list.html'

    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    company_id = user_token_company[0]['company_id']

    objects = StockService.objects.filter(company_id=company_id)
    objects_paginator = Paginator(objects, registers_for_page)
    page_number = request.GET.get('page')
    page = objects_paginator.get_page(page_number)
    url_page = 'stock:stock_service_list'

    context =   {
                    'title': title,
                    'subtitle': subtitle,
                    'user_login': request.user,
                    'url_add': 'stock:stock_service_add',
                    'object_list': objects,
                    'page': page,
                    'url_page': url_page
                }
    return render(request, template_name, context)
    

@login_required(login_url='/auth/login/')
def stock_shopping_list(request):
    title = sig + 'Compras'
    subtitle = 'Compras'
    template_name = 'stock_list.html'

    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    company_id = user_token_company[0]['company_id']

    objects = StockShopping.objects.filter(company_id=company_id)
    objects_paginator = Paginator(objects, registers_for_page)
    page_number = request.GET.get('page')
    page = objects_paginator.get_page(page_number)
    url_page = 'stock:stock_shopping_list'

    context =   {
                    'title': title,
                    'subtitle': subtitle,
                    'user_login': request.user,
                    'url_add': 'stock:stock_shopping_add',
                    'object_list': objects,
                    'page': page,
                    'url_page': url_page
                }
    return render(request, template_name, context)
    

@login_required(login_url='/auth/login/')
def stock_production_list(request):
    title = sig + 'Produção'
    subtitle = 'Produção'
    template_name = 'stock_list.html'

    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    company_id = user_token_company[0]['company_id']

    objects = StockProduction.objects.filter(company_id=company_id)
    objects_paginator = Paginator(objects, registers_for_page)
    page_number = request.GET.get('page')
    page = objects_paginator.get_page(page_number)
    url_page = 'stock:stock_production_list'

    context =   {
                    'title': title,
                    'subtitle': subtitle,
                    'user_login': request.user,
                    'url_add': 'stock:stock_production_add',
                    'object_list': objects,
                    'page': page,
                    'url_page': url_page
                }
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def stock_inventary_list(request):
    title = sig + 'Inventário'
    subtitle = 'Inventário'
    template_name = 'stock_list.html'

    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    company_id = user_token_company[0]['company_id']

    objects = StockInventary.objects.filter(company_id=company_id)
    objects_paginator = Paginator(objects, registers_for_page)
    page_number = request.GET.get('page')
    page = objects_paginator.get_page(page_number)
    url_page = 'stock:stock_inventary_list'

    context =   {
                    'title': title,
                    'subtitle': subtitle,
                    'user_login': request.user,
                    'url_add': 'stock:stock_inventary_add',
                    'object_list': objects,
                    'page': page,
                    'url_page': url_page
                }
    return render(request, template_name, context)
    

#######################################################

@login_required(login_url='/auth/login/')
def stock_detail(request, pk, obj, template_name, url, title, subtitle):
    context =   {
                    'title': title,
                    'subtitle': subtitle,
                    'user_login': request.user,
                }
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def stock_sale_detail(request, pk):
    title = sig + 'Vendas'
    subtitle = 'Vendas'
    template_name = 'stock_detail.html'
    url_list = 'stock:stock_sale_list'
    obj = StockSale.objects.get(pk=pk)
    context =   {
                    'title': title,
                    'subtitle': subtitle,
                    'user_login': request.user,
                    'url_list': url_list,
                    'object': obj,
                    'pk': pk
                }
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def stock_service_detail(request, pk):
    title = sig + 'Serviços'
    subtitle = 'Serviços'
    template_name = 'stock_detail.html'
    url_list = 'stock:stock_service_list'
    obj = StockService.objects.get(pk=pk)
    context =   {
                    'title': title,
                    'subtitle': subtitle,
                    'user_login': request.user,
                    'url_list': url_list,
                    'object': obj,
                    'pk': pk
                }
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def stock_shopping_detail(request, pk):
    title = sig + 'Compras'
    subtitle = 'Compras'
    template_name = 'stock_detail.html'
    url_list = 'stock:stock_shopping_list'
    obj = StockShopping.objects.get(pk=pk)
    context =   {
                    'title': title,
                    'subtitle': subtitle,
                    'user_login': request.user,
                    'url_list': url_list,
                    'object': obj,
                    'pk': pk
                }
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def stock_production_detail(request, pk):
    title = sig + 'Produção'
    subtitle = 'Produção'
    template_name = 'stock_detail.html'
    url_list = 'stock:stock_production_list'
    obj = StockProduction.objects.get(pk=pk)
    context =   {
                'title': title,
                'subtitle': subtitle,
                'user_login': request.user,
                'url_list': url_list,
                'object': obj,
                'pk': pk
            }
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def stock_inventary_detail(request, pk):
    title = sig + 'Inventário'
    subtitle = 'Inventário'
    template_name = 'stock_detail.html'
    url_list = 'stock:stock_inventary_list'
    obj = StockInventary.objects.get(pk=pk)
    context =   {
                'title': title,
                'subtitle': subtitle,
                'user_login': request.user,
                'url_list': url_list,
                'object': obj,
                'pk': pk
            }
    return render(request, template_name, context)


#######################################################
@login_required(login_url='/auth/login/')
def stock_add(request, template_name, movimento, tipo_movimento, url, form, title, subtitle):
    estoque_form = Estoque()
    item_estoque_formset = inlineformset_factory(
        Estoque,    
        EstoqueItens,
        form=form,
        extra=0,
        min_num=1,
        validate_min=True,
    )
    if request.method == 'POST':
        form = EstoqueForm(request.user, request.POST, instance=estoque_form, prefix='main')
        formset = item_estoque_formset(
            request.POST,
            instance=estoque_form,
            prefix='estoque'
        )
        if form.is_valid() and formset.is_valid():
            form = form.save(commit=False)
            form.funcionario = request.user
            form.movimento = movimento
            form.tipo_movimento = tipo_movimento
            form.save()
            formset.save()
            stock_moviment(form)
            return {'pk': form.pk}
    else:
        form = EstoqueForm(request.user, instance=estoque_form, prefix='main')
        formset = item_estoque_formset(instance=estoque_form, prefix='estoque')
    context =   {
                    'form': form, 
                    'formset': formset,
                    'user_login': request.user,
                    'title': title, 
                    'subtitle': subtitle,
                }
    return context


@login_required(login_url='/auth/login/')
def stock_sale_add(request):
    title = sig + 'Vendas'
    subtitle = 'Vendas'
    template_name = 'stock_form_sale.html'
    url = 'stock:stock_sale_detail'
    movimento = 'S'
    tipo_movimento = 'V'
    form=EstoqueItensSaidaForm

    context = stock_add(request, template_name, movimento, tipo_movimento, url, form, title, subtitle)
    if context.get('pk'):
        return HttpResponseRedirect(resolve_url(url, context.get('pk')))
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def stock_service_add(request):
    title = sig + 'Serviços'
    subtitle = 'Serviços'
    template_name = 'stock_form_service.html'
    url = 'stock:stock_service_detail'
    movimento = 'S'
    tipo_movimento = 'S'
    form=EstoqueItensSaidaForm

    context = stock_add(request, template_name, movimento, tipo_movimento, url, form, title, subtitle)
    if context.get('pk'):
        return HttpResponseRedirect(resolve_url(url, context.get('pk')))
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def stock_shopping_add(request):
    title = sig + 'Compras'
    subtitle = 'Compras'
    template_name = 'stock_form_shopping.html'
    url = 'stock:stock_shopping_detail'
    movimento = 'E'
    tipo_movimento = 'C'
    form=EstoqueItensEntradaForm

    context = stock_add(request, template_name, movimento, tipo_movimento, url, form, title, subtitle)
    if context.get('pk'):
        return HttpResponseRedirect(resolve_url(url, context.get('pk')))
    return render(request, template_name, context)
        

@login_required(login_url='/auth/login/')
def stock_production_add(request):
    title = sig + 'Produção'
    subtitle = 'Produção'
    template_name = 'stock_form_production.html'
    url = 'stock:stock_production_detail'
    movimento = 'E'
    tipo_movimento = 'P'
    form=EstoqueItensEntradaForm

    context = stock_add(request, template_name, movimento, tipo_movimento, url, form, title, subtitle)
    if context.get('pk'):
        return HttpResponseRedirect(resolve_url(url, context.get('pk')))
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def stock_inventary_add(request):
    title = sig + 'Inventário'
    subtitle = 'Inventário'
    template_name = 'stock_form_inventary.html'
    url = 'stock:stock_inventary_detail'
    movimento = 'E'
    tipo_movimento = 'I'
    form=EstoqueItensEntradaForm

    context = stock_add(    
                            request, template_name, movimento, tipo_movimento, 
                            url, form, title, subtitle
                        )
    if context.get('pk'):
        return HttpResponseRedirect(resolve_url(url, context.get('pk')))
    return render(request, template_name, context)


#######################################################
def stock_moviment(form):
    # Pega os produtos a partir da instância do formulário (Estoque).
    produtos = form.estoques.all()
    for item in produtos:
        produto = Item.objects.get(pk=item.produto.pk)
        produto.stock_qtd = item.saldo
        produto.save()
