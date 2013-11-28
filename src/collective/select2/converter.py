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
        if value is self.field.missing_value:
            return u''
        return ','.join(value)

    def toFieldValue(self, value):
        """See interfaces.IDataConverter"""
        widget = self.widget
        if widget.terms is None:
            widget.updateTerms()
        get_term = lambda x: widget.terms.getValue(x)
        return [get_term(token) for token in value if get_term(token)]
