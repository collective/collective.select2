from zope.interface import implementer
from zope.schema import List
from .interfaces import ISelect2Field


@implementer(ISelect2Field)
class Select2Field(List):

    def __init__(self, value_type=None, unique=False, **kw):
        self.search_view = kw.pop('search_view', None)
        self.add_terms = kw.pop('add_terms', False)
        super(Select2Field, self).__init__(value_type, unique, **kw)
