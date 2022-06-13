from django import template

register = template.Library()

@register.simple_tag
def relative_url(field_name, value, urlencode=None):
    """
    Returns the current query strings plus the new query string
    wanted by the user
    """
    url = f'?{field_name}={value}'

    if urlencode:
        querystring = urlencode.split('&')
        def include_query_field(existing_query_field):
            return (
                existing_query_field.split('=')[0] != field_name and
                existing_query_field.split('=')[0] != 'page'
            )

        filtered_querystring = filter(include_query_field, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = f'{url}&{encoded_querystring}'
        if value == 'reset':
            url = f'?{encoded_querystring}'

    return url