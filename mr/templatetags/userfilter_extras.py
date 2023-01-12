from django import template
from django.contrib.auth.models import Group

from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

@register.filter(name='has_group')
def has_group(user, App_Admin):
    return user.groups.filter(name=App_Admin).exists()
