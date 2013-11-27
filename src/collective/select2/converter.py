import zope.schema
from z3c.form.converter import CollectionSequenceDataConverter

from z3c.form import util
from  .interfaces import IUserTokenInputWidget


class UserTokenConverter(CollectionSequenceDataConverter):
    """Data converter for IUserTokenInputWidget."""

    zope.component.adapts(
        zope.schema.interfaces.ISequence, IUserTokenInputWidget)

    def toWidgetValue(self, value):
        """Convert from text lines to HTML representation."""
        # if the value is the missing value, then an empty list is produced.
        if value is self.field.missing_value:
            return u''
        return value
