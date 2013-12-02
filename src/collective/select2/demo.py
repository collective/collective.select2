from zope import schema
from zope.interface import Interface
from zope.component.hooks import getSite
from z3c.form import field, form, button
from plone.z3cform.layout import wrap_form
# from .widget import UserTokenFieldWidget
from .widget import Select2FieldWidget
from .field import Select2Field


class ISchema(Interface):

    users = Select2Field(
        title=u"Users",
        value_type=schema.Choice(
            title=u"User ID",
            source="plone.app.vocabularies.Users"
        ),
        search_view=lambda x: '{}/select2-users-search'.format(x),
        required=True
    )

    categories = Select2Field(
        title=u"Categories",
        value_type=schema.Choice(
            title=u"Category",
            source="plone.app.vocabularies.Keywords"
        ),
        search_view=lambda x: '{}/select2-subjects-search'.format(x),
        add_terms=True,
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
