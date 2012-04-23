# -*- coding: utf-8 -*-
import logging

from z3c.form import form
from z3c.form import field
from z3c.form import button
from zope.interface import Interface

from vindula.chat import messageFactory as _
from vindula.chat.utils.setup import setupXMPPEnvironment

from zope.component import getUtility
from vindula.chat.interfaces import IPubSubStorage, IAdminClient

logger = logging.getLogger('vindula.chat')


class ISetupXMPP(Interface):
    pass


class SetupXMPPForm(form.Form):

    fields = field.Fields(ISetupXMPP)
    label = _("Setup XMPP")
    description = _("label_setup_warning",
        """
        Warning: This action should ONLY be run after the initial setup. It
        will create the necessary users and nodes on your XMPP server
        according to your plone site users. Unless you know what you are doing
        you do not need to run it again afterwards.
        Make sure you have set the correct settings for you XMPP server before
        submitting.
        """)

    ignoreContext = True

    @button.buttonAndHandler(_('Setup'), name='setup_xmpp')
    def setup_xmpp(self, action):
        data, errors = self.extractData()
        setupXMPPEnvironment(self.context)
