from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css):
    return field.as_widget(attrs={"class": css})

@register.filter
def attr(obj, attr_name):
    return getattr(obj, attr_name, None)