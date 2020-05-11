from django import template

register = template.Library()

@register.filter(name='split')
def split(value,key):
	d=str(value).split(key)
	return d