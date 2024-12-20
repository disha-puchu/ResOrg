from django import template
register = template.Library()

@register.filter()
def to_int(value):
   return int(value)

@register.filter()
def get_dict_val(dict, key):
   return dict[int(key)]
   
@register.filter()
def let(val):
   return val