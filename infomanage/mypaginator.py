# -*- coding: utf-8 -*-
# @Author: Fannie
from django.core.paginator import Paginator

class MyPaginator(Paginator):
    """docstring for MyPginator"""
    def __init__(self, object_list, per_pege, orpans=0, allow_empty_first_page=True, range_num=5):
        Paginator.__init__(self, object_list, per_pege, orpans, allow_empty_first_page)
        self.range_num = range_num

    def page(self, number):
        self.page_num = number
        return super(MyPaginator, self).page(number)

    def _page_range_ext(self):
        num_count = 2*self.range_num + 1
        if self.num_pages <= num_count:
            return range(1, self.num_pages+1)
        num_list = []
        num_list.append(self.page_num)
        for i in range(1, self.range_num+1):
            if self.page_num - i > 0:
                num_list.append(self.page_num-i)
            else:
                num_list.append(num_count + self.page_num - i)
            if self.page_num + i <= self.num_pages:
                num_list.append(self.page_num + 1)
            else:
                num_list.append(self.page_num + i - num_count)
        num_list.sort()
        return num_list
    page_range_ext = property(_page_range_ext)