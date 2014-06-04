from zope import schema
from zope.interface import Interface
from zope.component.hooks import getSite
from z3c.form import field, form, button
from plone.z3cform.layout import wrap_form

from .field import Select2MultiField
from .field import Select2Field


class ISchema(Interface):

    users = Select2MultiField(
        title=u"Users",
        value_type=schema.Choice(
            title=u"User ID",
            source="plone.app.vocabularies.Users"
        ),
        search_view=lambda x: '{}/select2-users-search'.format(x),
        required=True
    )

    user = Select2Field(
        title=u"Single User",
        source="plone.app.vocabularies.Users",
        search_view=lambda x: '{}/select2-users-search'.format(x),
        placeholder="Search and select a User",
        required=True
    )

    categories = Select2MultiField(
        title=u"Categories",
        value_type=schema.TextLine(
            title=u"Category"
        ),
        search_view=lambda x: '{}/select2-subjects-search'.format(x),
        required=False
    )


class Form(form.Form):
    fields = field.Fields(ISchema)
    ignoreContext = True

    @button.buttonAndHandler(u"Submit")
    def handleSave(self, __):
        data, errors = self.extractData()
        # import pdb; pdb.set_trace( )

View = wrap_form(Form)
