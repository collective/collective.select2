from zope.schema.interfaces import IChoice
from zope.interface import implementer
from zope.schema import List
from zope.schema import Choice
from .interfaces import ISelect2MultiField
from .interfaces import ISelect2Field


@implementer(ISelect2Field)
class Select2Field(Choice):

    def __init__(self, values=None, vocabulary=None, source=None, **kw):
        self.search_view = kw.pop('search_view', None)
        super(Select2Field, self).__init__(values, vocabulary, source, **kw)


@implementer(ISelect2MultiField)
class Select2MultiField(List):
    add_terms = True

    def __init__(self, value_type=None, unique=False, **kw):
        self.search_view = kw.pop('search_view', None)

        if IChoice.providedBy(value_type):
            self.add_terms = False

        super(Select2MultiField, self).__init__(value_type, unique, **kw)
