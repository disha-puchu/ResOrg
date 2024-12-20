from django import template
register = template.Library()

@register.filter()
def get_url_params(exp):
   list_params = exp.split('?')
   param_dict = {}
   for param in list_params:
      if param.find('=') == -1:
         param_dict['rid'] = int(param)
      else:
         key_value = param.split('=')
         param_dict[key_value[0]] = key_value[1]
   return param_dict

@register.filter()
def get_dict_val_str(dict, key):
   return dict[key]

@register.simple_tag
def getby_gname_rid(rlist, gname, rid, index):
   return rlist[gname][int(rid)][int(index)]

@register.simple_tag
def get_res(rlist, sid, rid, index):
   return rlist[int(sid)][int(rid)][index]


# @register.filter()
# def get_dict_val_bygname(dict, key):
#    return dict[key]
