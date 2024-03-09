from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from _gybase.constants import DEFAULT_PAGE_LIMIT



class BaseApiUtils:

    @staticmethod
    def get_paginator(page_number, data, limit=DEFAULT_PAGE_LIMIT):
        paginator = Paginator(data, limit)
        pagination = {}
        try:
            page = paginator.page(page_number)
            pagination['current_page'] = int(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
            pagination['current_page'] = 1
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
            pagination['current_page'] = paginator.num_pages
        pagination['total_pages'] = paginator.num_pages
        pagination['total_items'] = paginator.count
        pagination['page_size'] = limit
        return page.object_list, pagination

    @staticmethod
    def get_paging_object(page_number, item_count, limit=DEFAULT_PAGE_LIMIT):
        paginator = Paginator(range(item_count), limit)
        pagination = {}
        try:
            pagination['current_page'] = int(page_number)
        except Exception:
            pagination['current_page'] = 1
        pagination['total_pages'] = paginator.num_pages
        pagination['total_items'] = paginator.count
        pagination['page_size'] = limit
        return pagination

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip