from django.template import Library
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
import re

register = Library()

@stringfilter
@register.filter(name='spacesAndBR')
def spacesAndBR(value, autoescape=None):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    text1 = re.sub('\n', '<br>', value)
    text = re.sub('\s', '&'+'nbsp;', text1)
    return mark_safe(text)

spacesAndBR.needs_autoescape = True