# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from ftw.globalstatusmessage.interfaces import IStatusMessageConfigForm
from ftw.globalstatusmessage.interfaces import IStatusMessageAutomaticEnable
from ftw.globalstatusmessage.interfaces import IStatusMessageShowOnLogin
from ftw.globalstatusmessage.utils import is_path_included
from plone import api
from plone.app.layout.viewlets import common
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from zope.interface import implements


class StatusmessageViewlet(common.PathBarViewlet):
    index = ViewPageTemplateFile('statusmessage.pt')

    def update(self):
        super(StatusmessageViewlet, self).update()

    def render(self):
        registry = getUtility(IRegistry)
        self.settings = registry.forInterface(IStatusMessageConfigForm)

        if self.settings.enabled_automatic_bool:
            if not self.automatic_enable():
                return ''
        else:
            if not self.settings.enabled_bool:
                return ''

        if not self.settings.enabled_anonymous_bool and self.settings.show_on_login_bool:
            if self.show_on_login():
                return self.index()

        if api.user.is_anonymous() and not self.settings.enabled_anonymous_bool:
            return ''

        if not self.show_in_current_context():
            return ''

        return self.index()

    def automatic_enable(self):
        automatic_enable = getUtility(
                    IStatusMessageAutomaticEnable,
                    name='ftw.globalstatusmessage:automatic_enable')
        return automatic_enable()

    def show_on_login(self):
        if not api.user.is_anonymous():
            return False

        show_on_login = getUtility(
                    IStatusMessageShowOnLogin,
                    name='ftw.globalstatusmessage:show_on_login')
        return show_on_login(self.request)

    def show_in_current_context(self):
        excluded_site_paths = self.settings.exclude_sites or []
        if not excluded_site_paths:
            return True

        included_site_paths = set(self._all_sites_paths()) \
                              - set(excluded_site_paths)
        return is_path_included('/'.join(self.context.getPhysicalPath()),
                                included_site_paths,
                                excluded_site_paths)

    def _all_sites_paths(self):
        vocabulary_factory = getUtility(
            IVocabularyFactory,
            name='ftw.globalstatusmessage:sites_vocabulary')
        return [term.value for term in vocabulary_factory(None)]


class StatusmessageAutomaticEnable(object):
    """ Logic for the automatic enable option
    """
    implements(IStatusMessageAutomaticEnable)

    def __call__(self):
        return False

class StatusmessageShowOnLogin(object):
    """ Logic for the show on login form option
    """
    implements(IStatusMessageShowOnLogin)

    def __call__(self, kwargs):
        if '/login_form' in kwargs.get('URL', ''):
            return True
        elif '/login' in kwargs.get('URL', ''):
            return True
        else:
            return False
