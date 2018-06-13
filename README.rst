Introduction
============

With ``ftw.globalstatusmessage`` a Plone site administrator display messages
on all pages.

This is useful for inform the users about an upcoming maintance downtime or
any other important thing.

The message can be changed in the plone control panel:


.. image:: https://raw.githubusercontent.com/4teamwork/ftw.globalstatusmessage/master/docs/screenshot.png

Exclude sites
-------------

With the ``Exclude sites`` option it is possible to show the global status
message only for certain sub sites.
All containers providing the interface ``INavigationRoot`` are considered
sub sites. Make sure that the ``object_provides`` catalog index is up to date
after enabling the interface for a container.

When having nested sub sites, the nearest parent sub site relative to the
current context is relevant.
If the nearest sub site is not excluded but a parent is excluded, the message
is shown on the current context.

Allow automatic activation
--------------------------

With the ``Allow automatic activation?`` option active it is possible
to show and hide the global status message in automatic. By default, there is
no logic defined for this option. You can define your own utility
to specify the logic for the automatic activation as described bellow.

Under ``overrides.zcml`` register a utility as shown bellow:

::

    <utility
        name="ftw.globalstatusmessage:automatic_enable"
        provides="ftw.globalstatusmessage.interfaces.IStatusMessageAutomaticEnable"
        factory="mypackage.utilities.StatusmessageAutomaticEnable" />

and create a factory class for the automatic enable logic:

::
    from ftw.globalstatusmessage.interfaces import IStatusMessageAutomaticEnable
    from zope.interface import implements
    
    class StatusmessageAutomaticEnable(object):
        """ Global status message utility for automatic enable
        """
        implements(IStatusMessageAutomaticEnable)

        def __call__(self):
            return True

Show on login form
------------------

With the ``Show on login form?`` option active the global status message will
appear only on the ``login_form`` for the anonymous users. This option can be
useful for example when you want to inform your editors that the CMS login is
closed for maintenance. You can define your own utility to specify the logic
for detecting the login form as described bellow.

Under ``overrides.zcml`` register a utility as shown bellow:

::

    <utility
        name="ftw.globalstatusmessage:show_on_login"
        provides="ftw.globalstatusmessage.interfaces.IStatusMessageShowOnLogin"
        factory="mypackage.utilities.StatusmessageShowOnLogin" />

and create a factory class for the show on login form logic:

::
    from ftw.globalstatusmessage.interfaces import IStatusMessageShowOnLogin
    from zope.interface import implements
    
    class StatusmessageShowOnLogin(object):
        """ Global status message utility for show on login form
        """
        implements(IStatusMessageShowOnLogin)

        def __call__(self):
            return True

Compatibility
=============

Supports Plone `4.2`, `4.3`.


Installation
============

- Add ``ftw.globalstatusmessage`` to your buildout configuration:

::

    [instance]
    eggs +=
        ftw.globalstatusmessage

- Install the generic import profile.


Uninstall
=========

This package provides an uninstall Generic Setup profile.
Uninstall the package by using Plone's addon controlpanel or portal_quickInstaller.



Links
=====

- Github: https://github.com/4teamwork/ftw.globalstatusmessage
- Issues: https://github.com/4teamwork/ftw.globalstatusmessage/issues
- Pypi: http://pypi.python.org/pypi/ftw.globalstatusmessage
- Continuous integration: https://jenkins.4teamwork.ch/search?q=ftw.globalstatusmessage


Copyright
=========

This package is copyright by `4teamwork <http://www.4teamwork.ch/>`_.

``ftw.globalstatusmessage`` is licensed under GNU General Public License, version 2.
