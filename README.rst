.. contents::

Introduction
============

`Select2`_ integration for `Plone`_ and `z3c.form`_


Example::

    from zope import schema
    from zope.interface import Interface
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
            placeholder="Search and select a user",
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


.. _`Select2`: http://ivaynberg.github.io/select2/
.. _`Plone`: http://plone.org
.. _`z3c.form`: https://pypi.python.org/pypi/z3c.form
