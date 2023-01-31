from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from activation.models import TokenUser, Company
from .models import PartnerGroup, PartnerSubGroup, Partner, Category, UnMed, Item, Brand
from django.core.paginator import Paginator
from django.db.models import Sum


sig = 'SIG SANLIS | '
registers_for_page = 5


@login_required(login_url='/auth/login/')
def dashboard(request):
    title = sig + 'Painel'

    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    company_id = user_token_company_id[0][0]

    total = Item.objects.filter(company_id=company_id).aggregate(sum=Sum('stock_qtd'))
    stock_total = total

    context =   {   
                    'title': title,
                    'stock_total': stock_total,
                    'user_login': request.user
                }

    return render(request, 'painel.html', context)


############################################################
@login_required(login_url='/auth/login/')
def partners(request):
    title = sig + 'Lista de Parceiros'

    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    
    if user_token_company.exists():
        company_id = user_token_company_id[0][0]
        partners = Partner.objects.filter(company_id=company_id)
        groups = PartnerGroup.objects.filter(company_id=company_id)
        subgroups = PartnerSubGroup.objects.filter(company_id=company_id)
        
        nickname_filtrar = request.GET.get('nickname')
        if nickname_filtrar:
            partners = partners.filter(nickname__icontains = nickname_filtrar)

        groups_filtrar = request.GET.get('groups')
        if groups_filtrar:
            partners = partners.filter(group = groups_filtrar)

        subgroups_filtrar = request.GET.get('subgroups')
        if subgroups_filtrar:
            partners = partners.filter(subgroup = subgroups_filtrar)

        partners_paginator = Paginator(partners, registers_for_page)
        page_number = request.GET.get('page')
        page = partners_paginator.get_page(page_number)
        url_page = 'plataform:partners'

        context =   {   
                        'title': title,
                        'page': page,
                        'url_page': url_page,
                        'groups': groups,
                        'subgroups': subgroups,
                        'user_login': request.user
                    }
        render(request, 'partners/partner_list.html', context)

    elif user_token_company_id.count() == 0:
        messages.add_message(request, constants.ERROR, 'Não encontramos uma empresa para o seu usuário !!!')
        context =   {   
                        'title': title,
                        'user_login': request.user
                    }
        return redirect('/painel/')

    return render(request, 'partners/partner_list.html', context)


@login_required(login_url='/auth/login/')
def partner_create(request):
    title = sig + 'Criar Parceiro'

    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    company_id = user_token_company_id[0][0]

    groups = PartnerGroup.objects.filter(company_id=company_id)
    subgroups = PartnerSubGroup.objects.filter(company_id=company_id)
    
    context =   {   
                    'title': title,
                    'user_login': request.user,
                    'company_id_value': company_id,
                    'groups': groups,
                    'subgroups': subgroups
                }
    
    if request.method == "GET":
        return render(request, 'partners/partner_create.html', context)
    
    elif request.method == "POST":
        nickname = request.POST.get('nickname').upper()
        first_name = request.POST.get('first_name').upper()
        last_name = request.POST.get('last_name').upper()
        document = request.POST.get('document')
        email = request.POST.get('email').lower()
        phone1 = request.POST.get('phone1')
        phone2 = request.POST.get('phone2')

        company = request.POST.get('company')
        type_partners = request.POST.get('type_partners')
        type_person = request.POST.get('type_person')
        gender = request.POST.get('gender')
        group_id = request.POST.get('group')
        subgroup_id = request.POST.get('subgroup')
        status = "A"

        if (len(nickname.strip()) == 0):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos!!!')
            return render(request, 'partners/partner_create.html', context)

        partners = Partner.objects.filter(nickname=nickname)

        if partners.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um parceiro cadastrado com este nome!!!')
            return render(request, 'partners/partner_create.html', context)

        partner = Partner(  
                            nickname=nickname,
                            first_name=first_name,
                            last_name=last_name,

                            document=document,
                            phone1=phone1,
                            phone2=phone2,
                            email=email,

                            company_id=company,
                            type_partners=type_partners,
                            type_person=type_person,
                            gender=gender,
                            group_id=group_id,
                            subgroup_id=subgroup_id,
                            status=status
                            )
        partner.save()

        messages.add_message(request, constants.SUCCESS, 'Parceiro Cadastrado com Sucesso!!!')
        return render(request, 'partners/partner_create.html', context)


@login_required(login_url='/auth/login/')
def partner_view(request, id):
    title = sig + 'Visualizar Parceiro'

    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    company_id = user_token_company_id[0][0]

    groups = PartnerGroup.objects.filter(company_id=company_id)
    subgroups = PartnerSubGroup.objects.filter(company_id=company_id)

    partners_exists = Partner.objects.filter(id=id, company_id=company_id)
    if not partners_exists.exists():
        messages.add_message(request, constants.ERROR, 'Você não tem acesso a este identificador !!!')
        return redirect('/painel/parceiros')

    partner = get_object_or_404(Partner, id=id)

    return render(request, 'partners/partner_update.html', { 
                                                                'title': title,
                                                                'user_login': request.user,
                                                                'company_id_value': company_id,
                                                                'groups': groups,
                                                                'subgroups': subgroups,
                                                                'partner': partner,
                                                            })


@login_required(login_url='/auth/login/')
def partner_update(request, id):
    title = sig + 'Alterar Parceiro'
    
    nickname = request.POST.get('nickname')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    document = request.POST.get('document')
    email = request.POST.get('email')
    phone1 = request.POST.get('phone1')
    phone2 = request.POST.get('phone2')

    company = request.POST.get('company')
    type_partners = request.POST.get('type_partners')
    type_person = request.POST.get('type_person')
    gender = request.POST.get('gender')
    group_id = request.POST.get('group')
    subgroup_id = request.POST.get('subgroup')
    status = request.POST.get('status')

    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    company_id = user_token_company_id[0][0]

    groups = PartnerGroup.objects.filter(company_id=company_id)
    subgroups = PartnerSubGroup.objects.filter(company_id=company_id)

    partners_exists = Partner.objects.filter(id=id, company_id=company_id)
    if not partners_exists.exists():
        messages.add_message(request, constants.ERROR, 'Você não tem acesso a este identificador !!!')
        return redirect('/painel/parceiros')
    
    partner = Partner.objects.get(id=id)
    context =   {   
                    'title': title,
                    'groups': groups,
                    'subgroups': subgroups,
                    'partner': partner,
                }

    if (len(nickname.strip()) == 0):
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos !!!')
        return render(request, 'partners/partner_update.html', context)

    partners = Partner.objects.filter(id=id)
    if partners.exists():
        try:    
            partner.nickname = nickname
            partner.first_name = first_name
            partner.last_name = last_name
            partner.document = document
            partner.email = email
            partner.phone1 = phone1
            partner.phone2 = phone2

            partner.company_id = company
            partner.type_partners = type_partners
            partner.type_person = type_person
            partner.gender = gender
            partner.group_id = group_id
            partner.subgroup_id = subgroup_id
            partner.status = status

            partner.save()

            messages.add_message(request, constants.SUCCESS, 'Alteração Efetuada com Sucesso!')
            return redirect('/painel/parceiros')
        except:
            messages.add_message(request, constants.ERROR, 'Erro Interno do Sistema!!!')
            return redirect('/painel/parceiros')

    return render(request, 'partners/partner_list.html')


@login_required(login_url='/auth/login/')
def partner_delete(request, id):
    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    company_id = user_token_company_id[0][0]

    partners_exists = Partner.objects.filter(id=id, company_id=company_id)
    if not partners_exists.exists():
        messages.add_message(request, constants.ERROR, 'Você não tem acesso a este identificador !!!')
        return redirect('/painel/parceiros')
    else: 
        partner = Partner.objects.get(id=id)
        partner.delete()
        messages.add_message(request, constants.SUCCESS, 'Parceiro Excluído com Sucesso!')
        return redirect('/painel/parceiros')


############################################################
@login_required(login_url='/auth/login/')
def items(request):
    title = sig + 'Lista de Items'

    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    
    if user_token_company.exists():
        company_id = user_token_company_id[0][0]
        items = Item.objects.filter(company_id=company_id)
        categories = Category.objects.filter(company_id=company_id)
        un_meds = UnMed.objects.filter(company_id=company_id)
        brands = Brand.objects.filter(company_id=company_id)
        
        categories_filtrar = request.GET.get('categories')
        if categories_filtrar:
            items = items.filter(category = categories_filtrar)

        brands_filtrar = request.GET.get('brands')
        if brands_filtrar:
            items = items.filter(brand = brands_filtrar)

        title_filtrar = request.GET.get('title')
        if title_filtrar:
            items = items.filter(title__icontains = title_filtrar)

        items_paginator = Paginator(items, registers_for_page)
        page_number = request.GET.get('page')
        page = items_paginator.get_page(page_number)
        url_page = 'plataform:items'

        context =   {   
                        'title': title,
                        'page': page,
                        'url_page': url_page,
                        'categories': categories,
                        'un_meds': un_meds,
                        'brands': brands,
                        'user_login': request.user
                    }
        render(request, 'items/item_list.html', context)

    elif user_token_company_id.count() == 0:
        messages.add_message(request, constants.ERROR, 'Não encontramos uma empresa para o seu usuário !!!')
        context =   {   
                        'title': title,
                        'user_login': request.user
                    }
        return redirect('/painel/')

    return render(request, 'items/item_list.html', context)


@login_required(login_url='/auth/login/')
def item_create(request):
    title = sig + 'Criar Item'

    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    company_id = user_token_company_id[0][0]

    categories = Category.objects.filter(company_id=company_id)
    un_meds = UnMed.objects.filter(company_id=company_id)
    brands = Brand.objects.filter(company_id=company_id)
    
    context =   {   
                    'title': title,
                    'user_login': request.user,
                    'company_id_value': company_id,
                    'categories': categories,
                    'un_meds': un_meds,
                    'brands': brands
                }
    
    if request.method == "GET":
        return render(request, 'items/item_create.html', context)
    
    elif request.method == "POST":
        title = request.POST.get('title').upper()
        description = request.POST.get('description')
        location = request.POST.get('location')
        reference = request.POST.get('reference')

        stock_qtd1 = request.POST.get('stock_qtd')
        stock_qtd = 0 if stock_qtd1 == "" else request.POST.get('stock_qtd').replace(',', '.')

        price_in_cash1 = request.POST.get('price_in_cash')
        price_in_cash = 0 if price_in_cash1 == "" else request.POST.get('price_in_cash').replace(',', '.')
        
        price_term1 = request.POST.get('price_term')
        price_term = 0 if price_term1 == "" else request.POST.get('price_term').replace(',', '.')

        price_promotion1 = request.POST.get('price_promotion')
        price_promotion = 0 if price_promotion1 == "" else request.POST.get('price_promotion').replace(',', '.')

        price_custom1 = request.POST.get('price_custom')
        price_custom = 0 if price_custom1 == "" else request.POST.get('price_custom').replace(',', '.')

        company_id = request.POST.get('company')
        stock_control = request.POST.get('stock_control')
        type_item = request.POST.get('type_item')
        un_med_id = request.POST.get('un_med')
        category_id = request.POST.get('category')
        brand_id = request.POST.get('brand')
        status = "A"

        if (len(title.strip()) == 0):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos!!!')
            return render(request, 'items/item_create.html', context)

        items = Item.objects.filter(title=title)

        if items.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um item cadastrado com este nome!!!')

        item = Item(    
                        title=title,
                        description=description,
                        location=location,
                        reference=reference,

                        stock_qtd=stock_qtd,
                        price_custom=price_custom,
                        price_in_cash=price_in_cash,
                        price_term=price_term,
                        price_promotion=price_promotion,

                        company_id=company_id,
                        stock_control=stock_control,
                        type_item=type_item,
                        un_med_id=un_med_id,
                        category_id=category_id,
                        brand_id=brand_id,
                        status=status
                    )
        item.save()

        messages.add_message(request, constants.SUCCESS, 'Item Cadastrado com Sucesso!!!')
        return render(request, 'items/item_create.html', context)


@login_required(login_url='/auth/login/')
def item_view(request, id):
    title = sig + 'Visualizar Item'

    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    company_id = user_token_company_id[0][0]

    items_exists = Item.objects.filter(id=id, company_id=company_id)
    if not items_exists.exists():
        messages.add_message(request, constants.ERROR, 'Você não tem acesso a este identificador !!!')
        return redirect('/painel/itens')

    item = get_object_or_404(Item, id=id)
    items = Item.objects.filter(company_id=company_id)

    categories = Category.objects.filter(company_id=company_id)
    un_meds = UnMed.objects.filter(company_id=company_id)
    brands = Brand.objects.filter(company_id=company_id)

    return render(request, 'items/item_update.html',    { 
                                                            'title': title,
                                                            'user_login': request.user,
                                                            'company_id': company_id,
                                                            'categories': categories,
                                                            'un_meds': un_meds,
                                                            'brands': brands,
                                                            'item': item,
                                                            'items': items
                                                        })


@login_required(login_url='/auth/login/')
def item_update(request, id):
    title = sig + 'Alterar Item'
    
    title = request.POST.get('title')
    description = request.POST.get('description')
    location = request.POST.get('location')
    reference = request.POST.get('reference')

    stock_qtd1 = request.POST.get('stock_qtd')
    stock_qtd = 0 if stock_qtd1 == "" else request.POST.get('stock_qtd').replace(',', '.')

    price_custom1 = request.POST.get('price_custom')
    price_custom = 0 if price_custom1 == "" else request.POST.get('price_custom').replace(',', '.')

    price_in_cash1 = request.POST.get('price_in_cash')
    price_in_cash = 0 if price_in_cash1 == "" else request.POST.get('price_in_cash').replace(',', '.')

    price_term1 = request.POST.get('price_term')
    price_term = 0 if price_term1 == "" else request.POST.get('price_term').replace(',', '.')

    price_promotion1 = request.POST.get('price_promotion')
    price_promotion = 0 if price_promotion1 == "" else request.POST.get('price_promotion').replace(',', '.')

    company_id = request.POST.get('company')
    stock_control = request.POST.get('stock_control')
    type_item = request.POST.get('type_item')
    un_med_id = request.POST.get('un_med')
    category_id = request.POST.get('category')
    brand_id = request.POST.get('brand')
    status = request.POST.get('status')

    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    company_id = user_token_company_id[0][0]

    items_exists = Item.objects.filter(id=id, company_id=company_id)
    if not items_exists.exists():
        messages.add_message(request, constants.ERROR, 'Você não tem acesso a este identificador !!!')
        return redirect('/painel/itens')

    categories = Category.objects.filter(company_id=company_id)
    un_meds = UnMed.objects.filter(company_id=company_id)
    brands = Brand.objects.filter(company_id=company_id)
    
    item = Item.objects.get(id=id)
    items = Item.objects.filter(id=id)
    context =   {   
                    'title': title,
                    'categories': categories,
                    'un_meds': un_meds,
                    'brands': brands,
                    'item': item,
                    'items': items
                }

    if (len(title.strip()) == 0):
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos !!!')
        return render(request, 'items/item_update.html', context)

    if items.exists():
            item.title = title
            item.description = description
            item.location = location
            item.reference = reference

            item.stock_qtd = stock_qtd
            item.price_custom = price_custom
            item.price_in_cash = price_in_cash
            item.price_term = price_term
            item.price_promotion = price_promotion

            item.company_id = company_id
            item.stock_control = stock_control
            item.type_item = type_item
            item.un_med_id = un_med_id
            item.category_id = category_id
            item.brand_id = brand_id
            item.status = status

            item.save()

            messages.add_message(request, constants.SUCCESS, 'Alteração Efetuada com Sucesso!')
            return redirect('/painel/itens')
    return render(request, 'itens/item_list.html')


@login_required(login_url='/auth/login/')
def item_delete(request, id):
    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    company_id = user_token_company_id[0][0]

    items_exists = Item.objects.filter(id=id, company_id=company_id)
    if not items_exists.exists():
        messages.add_message(request, constants.ERROR, 'Você não tem acesso a este identificador !!!')
        return redirect('/painel/itens')
    else: 
        item = Item.objects.get(id=id)
        item.delete()
        messages.add_message(request, constants.SUCCESS, 'Item Excluído com Sucesso!')
        return redirect('/painel/itens')


############################################################
@login_required(login_url='/auth/login/')
def un_med_create(request):
    title = sig + 'Criar Item'
    user_login = User.objects.filter(username=request.user)
    users = User.objects.all()

    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    company_id_value = user_token_company_id[0][0]

    context =   {   'title': title,
                    'user_login': user_login[0],
                    'company_id_value': company_id_value,
                    'users': users}
    if request.method == "GET":
        return render(request, 'items/item_create.html', context)
    elif request.method == "POST":
        return render(request, 'items/item_create.html', context)


@login_required(login_url='/auth/login/')
def category_create(request):
    title = sig + 'Criar Item'
    user_login = User.objects.filter(username=request.user)
    users = User.objects.all()

    user_token_company = TokenUser.objects.filter(user_id=request.user).values('company_id')
    user_token_company_id = user_token_company.values_list('company_id')
    company_id_value = user_token_company_id[0][0]

    context =   {   'title': title,
                    'user_login': user_login[0],
                    'company_id_value': company_id_value,
                    'users': users}
    if request.method == "GET":
        return render(request, 'items/item_create.html', context)
    elif request.method == "POST":
        return render(request, 'items/item_create.html', context)


############################################################
# Ajax para Saldo
def produto_json(request, pk):
    ''' Retorna o produto, id e estoque. '''
    produto = Item.objects.filter(pk=pk)
    data = [item.to_dict_json() for item in produto]
    return JsonResponse({'data': data})
