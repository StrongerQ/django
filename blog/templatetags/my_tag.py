#email: strongeren@163.com
#_autor: smallqiang
from django import template
register = template.Library()

@register.simple_tag
def my_add(x):
    return x+100

@register.filter
def filter_add(x,y):
    return x+100+y