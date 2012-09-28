********************************
Example Plone Developement Tools
********************************

This collective package is created for the Plone Conf 2012 talk, Essential Development Tools. This
document discusses the tools that can be use during developtment. Snippets and examples are used to
explain how to tools can be used.

This document and the Plone conference talk is aimed at beginning and intermediate Plone developers. More
experienced developer are probably familiar with mentoined development tools.

Setting up Plone projects
=========================
When developing in Plone Templer is a tool which allows you to  generate code skeletons from
pre-defined templates. Skeletons for Python eggs, buildouts and Plone products can be created
using Templer.

.. topic:: To pip or not to pip
    When installing templer via the pip installer it's possible that the installation of templer
    and dependencies will fail. To circumvent this use easy_install instead, this installer
    correctly installs templer and dependencies

This snipper shows how to install templer in a virtual environment and list available skeletons:

    .. code-block:: console

        # virtualenv-2.7 templer-example
        # cd templer-example/
        # . ./bin/activate
        # easy_install templer.plone templer.plone.localcommands
        # templer --list

This snippet shows how to create a Dexterity-based project with ZopeSkel. Templer does not yet
have the functionality to create such projects:

    .. code-block:: console

        # virtualenv-2.7 dexterity-example
        # cd dexterity-example
        # . ./bin/activate
        # easy_install ZopeSkel==2.21.2  Paste PasteDeploy PasteScript zopeskel.dexterity
        # ./bin/zopeskel dexterity

More information about Templer and ZopeSkel:

 * http://blog.jazkarta.com/2012/07/12/templer-and-zopeskel/
 * http://blog.aclark.net/2012/07/12/the-plones-templer/

Speed up buildout
=================

.. figure:: http://fschulze.github.com/mr.developer/xkcd-buildout.png

::

    Let Mr. Developer help you win the everlasting buildout battle!
    (Remixed by Matt Hamilton, original from http://xkcd.com/303

When running a (fresh) buildout it can take while before it's finished. Using a few tricks it's possible
  to increase the buildout speed.

 * Use buildout.dumppickedversions 0.5 or later
 * Use zc.buildout version 1.5 or later
 * Use the -N option
 * Clean out egg cache and use virtualenv

More detailed information about buildout performance improvements can be found here: http://rpatterson.net/blog/buildout-performance-improvements

Another way to speed up buildout is to restrict the which server can be used to download eggs. Using this
restriction buildout is only allowed to connect to certain servers. When running a buildout without allowed
hosts buildout can be slowed down on slow Python egg repositories.

    .. code-block:: cfg

        [buildout]
        ...
        allow-hosts =
            pypi.python.org
            dist.plone.org

Alternatively a connection timeout can be set when running buildout:

    .. code-block:: console

        bin/buildout -t 5

Manage development eggs with mr.developer
=========================================
The buildout extension `mr.developer <http://pypi.python.org/pypi/mr.developer>`_ manages development
eggs in a buildout. When developing on a Plone project, Python eggs and/or Plone products can be added
from a revision control repository such as Git or Subversion.

Mr.developer usage has the following benefits opposed to a manual checkout:

 * When buildout is run for the first time the egg are automatically checked out. No need for a manual checkout of the development eggs.
 * Bulk update the developement eggs
 * More?...

In the snippet below `collective.developermanual <http://collective-docs.readthedocs.org/>`_ is added as
an develop egg:

   .. code-block:: cfg

        [buildout]
        extensions =
            mr.developer

         sources = sources
         # List products under development here
         auto-checkout +=
            https://github.com/collective/collective.developermanual.git

        [sources]
        collective.developermanual = git https://github.com/collective/collective.developermanual.git

Alternatively a development egg can be given without using mr.developer.

   .. code-block:: cfg

        [buildout]

        develop =
            src/collective.developermanual

Auto restart Plone using sauna.reload
=====================================

The Plone instance needs to be restarted when your source code is changed. The
`sauna.reload <http://pypi.python.org/pypi/sauna.reload>`_ add-on automatically restarts
Plone when source code is changed. This is a serious time saver when developing in Plone.


Add sauna.reload to the (Plone) instance part of your buildout
   .. code-block:: cfg

        [instance]
        zope-conf-additional = %import sauna.reload
        eggs +=
            sauna.reload

When sauna.reload is installed, an environment variable with the path to the development eggs
is given. This way sauna.reload knows which files need to be monitored for changes.

    .. code-block:: console

        # RELOAD_PATH=src/ bin/instance fg


Use Omelette to create a unified directory structure of installed packaged
==========================================================================
and 'use the source (luke)' to search in Plone core packages


Use plone.app.debugbar
======================

Dive into pdb when an error is raised using Products.PDBDebugMode
=================================================================

Products.PDBDebugMode

Do the PDB anywhere in your Plone site with Clouseau
====================================================


Debug a frozen Plone site
==================================================
 instance using Products.signalstack




Ease the releasing of eggs with jarn.mkrelease or zest.mkrelease
================================================================


Run your tests on jenkins or travis.ci for continious integration
=================================================================


