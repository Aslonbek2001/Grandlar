from django import template

register = template.Library()

@register.filter
def verbose_name(instance, field_name):
    try:
        return instance._meta.get_field(field_name).verbose_name
    except:
        return field_name