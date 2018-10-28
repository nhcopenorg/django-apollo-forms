from django.template.library import Library
from django.template.defaultfilters import stringfilter
import bleach
import simplejson as json
from six import string_types

# from fobi.helpers import two_dicts_to_string

register = Library()


@register.filter(is_safe=True)
@stringfilter
def apollo_format_data_form(jsonValue):
    data = json.loads(jsonValue)
    htmlData = "<div>{0}</div>"
    result = ""
    for key, value in data.items():
        result = result + htmlData.format("<div><strong>{0}</strong>: {1}</div>".format(key, value))

    """
    headers = json.loads(Asset.form_data_headers)
    data = json.loads(Asset.saved_data)
    """
    """
    headers = json.loads(value).keys()
    for key, value in data.items():

        if isinstance(value, string_types):
            value = bleach.clean(value, strip=True)
            if (value.startswith('') or
                    value.startswith('http://') or
                    value.startswith('https://')):
                value = '<a href="{value}">{value}</a>'.format(
                    value=value
                )
            data[key] = value
    """
    return result


@register.filter(is_safe=False)
@stringfilter
def apollo_modal_id_format(form_name, form_id):
    return form_name + str(form_id)
