********************************
Example Plone Developement Tools
********************************

This package is created for the Plone Conf 2012 talk, Essential Development Tools. When developing a
Plone product there are tools available which can ease development. This package will cover the technical
aspects of the tools and how to apply them.

This document will show how to use the tools by using examples. It isn't guaranteed that the information
here is up-to-date fot the please read the Collective Developer Manual.


Setting up a project using templer (or paster)
==============================================
Templer is used for setting up Python eggs or buildouts. Paster is templers predecessor.

.. topic:: To pip or not to pip
    When installing templer via the pip installer it's possible that the installation of templer
    and dependencies will fail. To circumvent this use easy_install instead, this installer
    correctly installs templer and dependencies

https://github.com/collective/ZopeSkel/issues/4

This snipper shows how to install templer in a virtual environment:

    .. code-block:: console

        # virtualenv-2.7 templer-example
        # cd templer-example/
        # . ./bin/activate
        # easy_install templer.plone templer.plone.localcommands
        # templer --list




Speed up buildout
=================

.. figure:: http://fschulze.github.com/mr.developer/xkcd-buildout.png

    Let Mr. Developer help you win the everlasting buildout battle!

    (Remixed by Matt Hamilton, original from http://xkcd.com/303)

Use allow hosts in buildout to speed up downloading of eggs
Use a default.cfg in your buildout to centralize eggs and download caches

Also see: http://blog.aclark.net/2012/08/13/bootstrapping-a-buildout-1-6-release/

Creating buildouts and products using paster or templer


Manage development eggs with mr.developer
=========================================

Mr.developer helps with development eggs, auto-checkout and updating all eggs.
Other tips and tricks

http://pypi.python.org/pypi/mr.developer

Automatically restart using sauna.reload
========================================




Use Omelette to create a unified directory structure of installed packaged
==========================================================================
and 'use the source (luke)' to search in Plone core packages


Use plone.app.debugbar
======================

Dive into pdb when an error is raised using Products.PDBDebugMode
=================================================================

Do the PDB anywhere in your Plone site with Clouseau
====================================================


Debug a frozen instance using Products.signalstack
==================================================



Ease the releasing of eggs with jarn.mkrelease or zest.releaser
===============================================================


Run your tests on jenkins or travis.ci for continious integration
=================================================================


