import json
import zope.interface
from zope.component.hooks import getSite
from z3c.form import interfaces
from z3c.form.widget import SequenceWidget
from z3c.form.widget import FieldWidget
from z3c.form.browser import widget

from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from .interfaces import ISelect2Widget


class Select2Widget(widget.HTMLTextInputWidget, SequenceWidget):
    zope.interface.implementsOnly(ISelect2Widget)
    input_template = ViewPageTemplateFile('input.pt')
    klass = u"select2-widget"

    @property
    def search_url(self):
        search_view = self.field.search_view
        if callable(search_view):
            portal = getSite()
            return search_view(portal.absolute_url())
        return search_view

    @property
    def initial_values(self):
        values = {}
        if self.value:
            base = self.value
            if not isinstance(base, list):
                base = self.value.split(',')
            for token in base:
                try:
                    term = self.terms.getTermByToken(token)
                except LookupError:
                    continue

                if term.title:
                    values[token] = term.title
        return json.dumps(values)

    def extract(self, default=interfaces.NO_VALUE):
        """See z3c.form.interfaces.IWidget."""
        value = self.request.get(self.name, default)
        if value != u'' and value != default:
            value = value.split(',')
            for token in value:
                if token == self.noValueToken:
                    continue
                try:
                    self.terms.getTermByToken(token)
                except LookupError:
                    return default
        return value


@zope.interface.implementer(interfaces.IFieldWidget)
def Select2FieldWidget(field, value_type, request):
    """IFieldWidget factory for Select2Widget."""
    return FieldWidget(field, Select2Widget(request))
