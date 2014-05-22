import json
import zope.interface
from zope.component.hooks import getSite
from z3c.form import interfaces
from z3c.form.widget import SequenceWidget
from z3c.form.widget import Widget
from z3c.form.browser.select import SelectWidget
from z3c.form.widget import FieldWidget
from z3c.form.browser import widget

from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from .interfaces import ISelect2Widget
from .interfaces import ISelect2MultiWidget
from .interfaces import ISelect2CollectionWidget


class BaseSelect2Widget(widget.HTMLTextInputWidget):
    input_template = ViewPageTemplateFile('input.pt')
    klass = u"select2-multi-widget"

    @property
    def initial_values(self):
        return {}

    def placeholder(self):
        return self.field.placeholder

    @property
    def search_url(self):
        search_view = self.field.search_view
        if callable(search_view):
            portal = getSite()
            return search_view(portal.absolute_url())
        return search_view

    @property
    def formatted_value(self):
        if isinstance(self.value, (tuple, list)):
            return ','.join(self.value)
        return self.value


@zope.interface.implementer_only(ISelect2Widget)
class Select2Widget(BaseSelect2Widget, SelectWidget):
    klass = u"select2-widget"

    @property
    def initial_values(self):
        values = {}
        if self.value:
            token = self.value
            if isinstance(token, (tuple, list)):
                token = token[0]
            try:
                term = self.terms.getTermByToken(token)
                values[token] = term.title
            except LookupError:
                pass

        return json.dumps(values)


@zope.interface.implementer(interfaces.IFieldWidget)
def Select2FieldWidget(field, request):
    """IFieldWidget factory for Select2MultiWidget."""
    return FieldWidget(field, Select2Widget(request))


@zope.interface.implementer_only(ISelect2MultiWidget)
class Select2MultiWidget(BaseSelect2Widget, Widget):

    @property
    def initial_values(self):
        values = {}
        if self.value:
            base = self.value
            if not isinstance(base, list):
                base = self.value.split(',')
            values = {}
            for token in base:
                values[token] = token

        return json.dumps(values)

    def extract(self, default=interfaces.NO_VALUE):
        value = self.request.get(self.name, default)
        if value != u'' and value != default:
            return value.split(',')

        if not isinstance(value, list):
            return []


@zope.interface.implementer(interfaces.IFieldWidget)
def Select2MultiFieldWidget(field, value_type, request):
    """IFieldWidget factory for Select2MultiWidget."""
    return FieldWidget(field, Select2MultiWidget(request))


@zope.interface.implementer_only(ISelect2CollectionWidget)
class Select2CollectionWidget(BaseSelect2Widget, SequenceWidget):

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
def Select2CollectionFieldWidget(field, value_type, request):
    """IFieldWidget factory for Select2CollectionWidget."""
    return FieldWidget(field, Select2CollectionWidget(request))
