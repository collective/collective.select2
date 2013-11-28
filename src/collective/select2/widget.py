import json
import zope.interface
from zope.component.hooks import getSite
from z3c.form import interfaces
from z3c.form.widget import SequenceWidget
from z3c.form.widget import FieldWidget
from z3c.form.browser import widget

from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from .interfaces import IUserTokenInputWidget


class UserTokenInputWidget(widget.HTMLTextInputWidget, SequenceWidget):
    zope.interface.implementsOnly(IUserTokenInputWidget)
    input_template = ViewPageTemplateFile('input.pt')
    klass = u"usertokeninput-widget"

    @property
    def usertoken_url(self):
        portal = getSite()
        return "{}/users_search".format(portal.absolute_url())

    def extract(self, default=interfaces.NO_VALUE):
        """See z3c.form.interfaces.IWidget."""
        value = self.request.get(self.name, default)
        if value != default:
            value = value.split(',')
            for token in value:
                if token == self.noValueToken:
                    continue
                try:
                    self.terms.getTermByToken(token)
                except LookupError:
                    return default
        return value

    def initialvalues(self):
        values = {}
        if self.value:
            for token in self.value.split(','):
                try:
                    term = self.terms.getTermByToken(token)
                except LookupError:
                    continue
                values[token] = term.title
        return json.dumps(values)


@zope.interface.implementer(interfaces.IFieldWidget)
def UserTokenInputFieldWidget(field, request):
    """IFieldWidget factory for UserTokenInputWidget."""
    return FieldWidget(field, UserTokenInputWidget(request))
