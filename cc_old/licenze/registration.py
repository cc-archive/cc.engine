"""Non-ZCML registrations for cc.licenze."""
from __future__ import absolute_import

from zope import component

from . import interfaces
from . import zero

# CC0
zero_chooser = zero.ZeroSelector()
component.provideUtility(zero_chooser, interfaces.ILicenseSelector, 'zero')
