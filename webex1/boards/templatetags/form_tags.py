from django import template
from django.template import Library
from django.template.defaulttags import cycle as cycle_original

register = Library()


register = template.Library()

@register.filter
def field_type(bound_field):
    return bound_field.field.widget.__class__.__name__

@register.filter
def input_class(bound_field):
    css_class = ''
    if bound_field.form.is_bound:
        if bound_field.errors:
            css_class = 'is-invalid'
        elif field_type(bound_field) != 'PasswordInput':
            css_class = 'is-valid'
    return 'form-control {}'.format(css_class)

@register.tag
def cycle(*args, **kwargs):
    ''' A stub to get SortableTabularInline to work '''
    return cycle_original(*args, **kwargs)