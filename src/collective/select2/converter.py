from z3c.form.converter import CollectionSequenceDataConverter
from z3c.form.converter import TextLinesConverter
from z3c.form import util


class Select2CollectionConverter(CollectionSequenceDataConverter):
    """Data converter for ISelect2CollectionWidget."""

    def toWidgetValue(self, value):
        """Convert from text lines to HTML representation."""

        if value is self.field.missing_value:
            return ()
        return value

    def toFieldValue(self, value):
        """See interfaces.IDataConverter"""
        widget = self.widget
        if widget.terms is None:
            widget.updateTerms()
        get_term = lambda x: widget.terms.getValue(x)
        return [get_term(token) for token in value if get_term(token)]


class Select2Converter(Select2CollectionConverter):

    def toFieldValue(self, value):
        """See interfaces.IDataConverter"""
        if value is self.field.missing_value:
            return []
        return value

    def toWidgetValue(self, value):
        if isinstance(value, (list, tuple)):
            return value
