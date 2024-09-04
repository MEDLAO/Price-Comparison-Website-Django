from django import template

register = template.Library()


@register.filter
def add(value, arg):
    try:
        return int(value) + int(arg)
    except (ValueError, TypeError):
        return ''


@register.filter
def get_by_id(queryset, product_id):
    return queryset.get(id=product_id)


@register.filter
def dict_get(dictionary, key):
    """
    Custom template filter to get a value from a dictionary using a key.
    Returns an empty list if the key is not found.
    """
    return dictionary.get(key, [])
