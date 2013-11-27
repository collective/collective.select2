from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer
from z3c.form import interfaces


class IBrowserLayer(IDefaultPloneLayer):
    pass


class ISelect2Widget(Interface):
    pass


class IUserTokenInputWidget(interfaces.IOrderedSelectWidget):
    """Marker interface for UserTokenInputWidget
    """
