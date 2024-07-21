from django import template
from datetime import datetime
from typing import Union

register = template.Library()

@register.filter
def l2l_dt(value: Union[str, datetime]) -> str:
    """
    Formats a date string or datetime object to the format '%Y-%m-%d %H:%M:%S'.
    
    Args:
        value string or datetime object: The date string with the format yyyy-mm-ddTH:M:S or datetime object to format.
    
    Returns:
        str: an datetime as an string with the format yyyy-mm-dd H:M:S.
    """
    try:
        l2l_date_format = "%Y-%m-%d %H:%M:%S"
        if isinstance(value, datetime):
            return value.strftime(l2l_date_format)

        str_original_date_format = "%Y-%m-%dT%H:%M:%S"
        _date = datetime.strptime(value, str_original_date_format)
        return _date.strftime(l2l_date_format)
    except (ValueError, TypeError):
        # TODO Add some logging
        return value
