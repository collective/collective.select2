from zope.interface import Interface
from zope.schema.interfaces import IList
from zope.schema._bootstrapfields import Field
from zope.schema._bootstrapfields import Bool
from plone.theme.interfaces import IDefaultPloneLayer
from z3c.form import interfaces


class IBrowserLayer(IDefaultPloneLayer):
    pass


class ISelect2Field(IList):
    """It inherits from IList and add to that field the search_view
    parameter

    Usage:

    >>> from zope.import schema
    >>> from zope.interface import Interface
    >>> from z3c.form import form, fields
    >>> from collective.select2.field import Select2Field
    >>> from collective.select2.widget import UserTokenFieldWidget

    >>> class ISchema(Interface):
    >>>     users = Select2Field(
    ...         title=u"Users",
    ...         value_type=schema.Choice(
    ...             title=u"User ID",
    ...             source="plone.app.vocabularies.Users"
    ...         ),
    ...     search_view='search_url',
    ...     add_terms=True,
    ...     required=True
    ... )

    >>> class Form(form.Form):
    ...     fields = field.Fields(ISchema)
    """

    search_view = Field(
        title=u"search_view",
        description=u""
    )

    add_terms = Bool(
        title=u'Add terms',
        description=u'',
        default=False
    )


class ISelect2Widget(interfaces.IOrderedSelectWidget):
    """Select2 widget for ISelect2Field
    """
