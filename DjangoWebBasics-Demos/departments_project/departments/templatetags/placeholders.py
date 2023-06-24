from django import template

register = template.Library()


@register.filter
def add_placeholder(value):
    print(value)
    p_list = value.name.split('_')

    return value.as_widget(attrs={'placeholder': ' '.join(s.capitalize() for s in p_list)})
