from django import template

register = template.Library()


@register.filter
def mediapath(image_url):
    if image_url:
        return f'/media/{image_url}'
    return '#'
