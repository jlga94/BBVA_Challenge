from django import template

register = template.Library()


@register.filter(name='add_class')
def add_class(field, classes):
    return field.as_widget(attrs={"class": classes})


@register.filter(name='add_class_form_control')
def add_class_form_control(field):
    return field.as_widget(attrs={"class": 'form-control'})


@register.filter(name='add_class_form_picker')
def add_class_form_picker(field):
    return field.as_widget(attrs={"class": 'form-control datepicker'})


@register.filter(name='add_class_form_select2')
def add_class_form_select2(field):
    return field.as_widget(attrs={"class": 'form-control select2'})


@register.filter(name='add_class_form_file')
def add_class_form_file(field):
    return field.as_widget(attrs={"class": 'file-styled'})


@register.filter(is_safe=True)
def add_class_label_tag(value):
    return value.label_tag(attrs={'class': arg})
