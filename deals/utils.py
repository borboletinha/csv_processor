from io import BytesIO, TextIOWrapper
from datetime import datetime
from itertools import chain

from django.db.models import F, Sum
from django_mysql.models import GroupConcat

from deals.models import Deal


def export_deals_in_db(file):
    file = BytesIO(file.read())
    reader = TextIOWrapper(file, encoding='utf-8').readlines()[1:]
    for row in reader:
        row = row.rstrip().split(',')
        deal, created = Deal.objects.get_or_create(
            customer=row[0],
            item=row[1],
            price=int(row[2]),
            quantity=int(row[3]),
            deal_date=datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S.%f'))
        deal.save()


def handle_data_queryset():

    # Get a main queryset
    deals = Deal.objects.values('customer').annotate(gems_raw=GroupConcat('item')).annotate(
        spent_money=Sum(F('price') * F('quantity'))).order_by('-spent_money')[:5]

    # Convert gems str to list
    for customer_deals in deals:
        customer_deals['gems_raw'] = list(set(customer_deals['gems_raw'].split(',')))

    # Get a list of all gems
    gems_list_nested = [customer_deals['gems_raw'] for customer_deals in deals]
    gems_list = list(chain.from_iterable(gems_list_nested))

    # Check if a gem was bought more than two times
    for customer_deals in deals:
        customer_deals['gems'] = []
        duplicates_remover = []
        for gem in gems_list:
            if gems_list.count(gem) >= 2 and gem in customer_deals['gems_raw'] and gem not in duplicates_remover:
                customer_deals['gems'].append(gem)
                duplicates_remover.append(gem)
        del customer_deals['gems_raw']

    return deals
