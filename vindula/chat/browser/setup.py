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
        Aviso: Esta ação deve ser executado somente após a configuração inicial. ele
         irá criar os usuários necessários em seu servidor XMPP
         de acordo com os usuários do site Plone. A menos que você saiba o que está fazendo
         você não precisa executá-lo novamente depois.
         Certifique-se de ter definido as configurações corretas para seu servidor XMPP antes
         submeter-se.
        """)

    ignoreContext = True

    @button.buttonAndHandler(_('Setup'), name='setup_xmpp')
    def setup_xmpp(self, action):
        data, errors = self.extractData()
        setupXMPPEnvironment(self.context)
