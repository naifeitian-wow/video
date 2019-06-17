from django import template
from video.models import TVModel


# 用来注册一个自定义的标签
register=template.Library()

from django.utils.html import format_html
@register.simple_tag
def circle_page(curr_page,loop_page,type,type2,country,year):
    offset = abs(curr_page - loop_page)
    if offset < 3:
        if curr_page == loop_page:
            page_ele = "<a class='select p' href='/list/{}/{}/{}/{}/{}/'>{}</a>".format(type,type2,country,year,loop_page,loop_page)
        else:
            page_ele = '<a class="p" href="/list/{}/{}/{}/{}/{}/">{}</a>'.format(type,type2,country,year,loop_page,loop_page)
        return format_html(page_ele)
    else:
        return ''

