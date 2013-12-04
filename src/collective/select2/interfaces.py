from zope.interface import Interface
from zope.schema.interfaces import IList
from zope.schema.interfaces import IChoice
from zope.schema._bootstrapfields import Field
from zope.schema._bootstrapfields import Bool
from plone.theme.interfaces import IDefaultPloneLayer
from z3c.form import interfaces


class IBrowserLayer(IDefaultPloneLayer):
    pass


class ISelect2Field(IChoice):
    """It inherits from IChoice and add to the field the search_view
    parameter
    """
    search_view = Field(
        title=u"search view url",
        description=u""
    )


class ISelect2MultiField(IList):
    """It inherits from IList and add to the field the search_view
    parameter

    Usage:

    >>> from zope.import schema
    >>> from zope.interface import Interface
    >>> from z3c.form import form, fields
    >>> from collective.select2.field import Select2MultiField
    >>> from collective.select2.widget import UserTokenFieldWidget

    >>> class ISchema(Interface):
    >>>     users = Select2MultiField(
    ...         title=u"Users",
    ...         value_type=schema.Choice(
    ...             title=u"User ID",
    ...             source="plone.app.vocabularies.Users"
    ...         ),
    ...     search_view='search_url',
    ...     required=True
    ... )

    >>> class Form(form.Form):
    ...     fields = field.Fields(ISchema)
    """

    search_view = Field(
        title=u"search view url",
        description=u""
    )


class ISelect2Widget(interfaces.ITextLinesWidget):
    """Select2 widget for ISelect2MultiField and value_type TextLine
    """


class ISelect2MultiWidget(interfaces.IOrderedSelectWidget):
    pass


class ISelect2CollectionWidget(ISelect2MultiWidget):
    """Select2 widget for ISelect2MultiField and value_type Choice
    """
