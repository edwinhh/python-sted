from django import template

register = template.Library()

@register.filter #最多就2个参数
def abc(s,length=10):
    if len(s)>length:
        s = s[:11]+'....'
    return s

@register.simple_tag
def abc2(s,length=10):
    if len(s)>length:
        s = s[:11]+'....'
    return s