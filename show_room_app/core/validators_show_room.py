from datetime import datetime

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_year(value):
    if value in range(1950, datetime.now().year + 1):
        raise ValidationError(
            _("%(value)s must be year"),
            params={"value": value},
        )
