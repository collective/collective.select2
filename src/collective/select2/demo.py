from zope import schema
from zope.interface import Interface
from z3c.form import field, form, button
from plone.z3cform.layout import wrap_form
from .widget import UserTokenInputFieldWidget


class ISchema(Interface):

    users = schema.List(
        title=u"Users",
        value_type=schema.Choice(
            title=u"User ID",
            source="plone.app.vocabularies.Users"
        ),
        required=False
    )


class Form(form.Form):
    fields = field.Fields(ISchema)
    fields['users'].widgetFactory = UserTokenInputFieldWidget
    ignoreContext = True

    @button.buttonAndHandler(u"Submit")
    def handleSave(self, __):
        data, errors = self.extractData()
        import pdb; pdb.set_trace( )

UserForm = wrap_form(Form)
