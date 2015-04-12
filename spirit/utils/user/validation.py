from __future__ import unicode_literals
import re

from django.conf import settings

def is_allowed_email(email):
    """
    Validates a string against the ALLOWED_EMAILS list of regular expressions. 
    """

    try:
        allowed = settings.ALLOWED_EMAILS
    except AttributeError:
        return True # Default to allowing all emails

    for pattern in allowed:
        if re.match(pattern,email):
            return True

    return False



