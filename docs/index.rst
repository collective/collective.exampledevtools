********************************
Example Plone Developement Tools
********************************

This collective package is created for the Plone Conf 2012 talk, Essential Development Tools. This
document discusses the tools that can be used during development. Snippets and examples are used to
explain how to tools can be used. For further installation and configuration details for these tools
please read the package details on pypi.python.org.

This document and the Plone conference talk aims at novice and intermediate Plone developers. More
experienced developers will probably be familiar with the development tools mentioned.

Setting up Plone projects
=========================
When developing in Plone, templer is a tool that allows you to generate code skeletons from
pre-defined templates. Skeletons for Python eggs, buildouts and Plone products can be created
using Templer.

.. topic:: To pip or not to pip
    When installing Templer via the pip installer, it's possible that the installation of templer
    and its dependencies will fail. To circumvent this, use easy_install instead. This installer
    will install templer and its dependencies correctly.

This snippet shows how to install templer in a virtual environment and list the available skeletons:

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

More information about creating an add-on packages can be found in this `getting started
document on readthedocs <http://collective-docs.readthedocs.org/en/latest/getstarted/index.html#creating-your-first-add-on>`_.


Speed up buildout
=================

.. figure:: http://fschulze.github.com/mr.developer/xkcd-buildout.png

::

    Let Mr. Developer help you win the everlasting buildout battle!
    (Remixed by Matt Hamilton, original from http://xkcd.com/303

When running a (fresh) buildout it can take while before it's finished. Using a few tricks it's possible to increase the buildout speed.

 * Use buildout.dumppickedversions 0.5 or later
 * Use zc.buildout version 1.5 or later
 * Use the -N option, buildout will not seek for packages with new versions
 * Clean out egg cache and use virtualenv

More detailed information about buildout performance improvements can be found here: http://rpatterson.net/blog/buildout-performance-improvements

Another way to speed up buildout is to restrict the which server can be used to download eggs. Using this
restriction buildout is only allowed to connect to certain servers. When running a buildout without allowed
hosts, buildout can be slowed down on slow Python egg repositories.

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

The use of Mr.developer has the following benefits opposed to a manual checkout:

 * When buildout is run for the first time, the eggs will automatically be checked out. No need for a manual checkout of the development eggs.
 * Bulk update the development eggs
 * Many `options for managing packages <http://pypi.python.org/pypi/mr.developer#commands>`_ from a version control system

In the snippet below, `collective.developermanual <http://collective-docs.readthedocs.org/>`_ is added as
an develop egg:

   .. code-block:: cfg

        [buildout]
        extensions =
            mr.developer

         sources = sources
         # List products under development here
         auto-checkout +=
            collective.developermanual 

        [sources]
        collective.developermanual = git https://github.com/collective/collective.developermanual.git

Alternatively, a development egg can be inserted in buildout configuration without using mr.developer.

   .. code-block:: cfg

        [buildout]

        develop =
            src/collective.developermanual

Auto restart Plone using sauna.reload
=====================================

The Plone instance needs to be restarted when your source code is changed. The
`sauna.reload <http://pypi.python.org/pypi/sauna.reload>`_ add-on automatically restarts
Plone when source code was changed. This is a serious time saver when developing in Plone.


Add sauna.reload to the (Plone) instance part of your buildout
   .. code-block:: cfg

        [instance]
        zope-conf-additional = %import sauna.reload
        eggs +=
            sauna.reload

When sauna.reload is installed, an environment variable with the path to the development eggs
needs to be included. This way, sauna.reload knows which files need to be monitored for changes.

    .. code-block:: console

        # RELOAD_PATH=src/ bin/instance fg

Omelette recipe
===============

Within a Plone buildout there are lots of namespaced packages. In a default buildout there is no easy way to navigate or
search for a specific part of code. The `collective.recipe.omelette <http://pypi.python.org/pypi//collective.recipe.omelette>`_
buildout extension creates a directory structure which resembles the Python namespaces of the installed packages.

This directory structure from omelette makes it easy to navigate in the packages and also makes it easy to issue a search (and
mumbering 'Use the Source Luke') for a specific piece of code in the omelette directory.

   .. code-block:: cfg

        [buildout]
        part += omelettte

        [omelette]
        recipe = collective.recipe.omelette
        eggs = ${instance:eggs}

Plone debug toolbar
===================

The `plone.app.debugtoolbar <http://pypi.python.org/pypi/plone.app.debugtoolbar>`_ provides
a wealth of development and debugging information about a running Plone site. The toolbar gives information
about the current object, request, workflow etc. etc. It provides an interactive Python prompt,
allowing you to debug thru-the-web.

To add the debug toolbar to Plone: add the package to the instance eggs and install it using the quick
installer.

Dummy mailhost
==============
When developing the `Products.PrintingMailHost <http://pypi.python.org/pypi/Products.PrintingMailHost>`_ add-on
can be used to display e-mails sent from Plone on standard out. PrintingMailHost monkey patches the Zope MailHost,
preventing mails to be sent out and printing the mail in the terminal.

::

    This is useful if you don't have a local mailhost for testing, or if you prefer not to spam
    the crap out of yourself whilst finding out if your bulk mail script is working.

To add the debug toolbar to Plone: add the package to the instance eggs.

Alternatively a dummy mail server can be run, which also displays mails on standard out:

   .. code-block:: console

        python -m smtpd -n -c DebuggingServer localhost:1025

Deprecated tools
================

The development tools mentioned in this section are deprecated. However they can be useful
when developing in older Plone versions (that is Plone 3 and older).

The `Products.PDBDebugMode <http://pypi.python.org/pypi/Products.PDBDebugMode>`_ package
provides a post-mortem debugger on exceptions. When an exception happens the Python pdb
debugger shows up in the terminal.

`Products.Clouseau <http://pypi.python.org/pypi/Products.Clouseau>`_ provides an interactive
Python prompt from a Plone site. The plone.app.debugtoolbar also provides this functionality.
It's recommended to use the debugtoolbar.


`plone.reload <http://pypi.python.org/pypi/plone.reload>`_ allows reloading of source code and zcml
without server restarts. This package is succeeded by sauna.reload for the latest version of Plone.

Debug a frozen Plone site
=========================

It's worrying when a Plone instance has become completely unresponsive (ie frozen by a deadlock).
There are multiple packages available to debug a frozen Plone instance. All packages have in common
that they can read out a stacktrace, allowing to pinpoint the cause of the freeze.

`Mr.freeze <http://pypi.python.org/pypi/mr.freeze>`_  can do several things. Provide a stacktrace
of the frozen instance, drop Zope to a pdb debug prompt and reload the source code or zcml.

`Products.signalstack <http://pypi.python.org/pypi/Products.signalstack>`_ is the predecessor of
mr.freeze. It has one function and that is dumping a stacktrace to the Zope log when a USR1
kill signal is sent.

Releasing eggs with jarn.mkrelease or zest.releaser
===============================================================

Releasing an egg to a Python egg index server (such as pypi.python.org) involves multiple steps: bumping the
version number, updating the history/changes file, tagging the release in version control,
creating the egg and uploading the egg to the index server.

Both `jarn.mkrelease <http://pypi.python.org/pypi/jarn.mkrelease>`_ and `zest.releaser <http://pypi.python.org/pypi/zest.releaser>`_ facilitate in releasing a Python egg. If you want to release an egg, it's easy to use one of these
release helper tools.

If you want to follow all steps mentioned in the release flow above, zest.release is more extensive than
jarn.mkrelease. However, if you only want to tag, package and upload the release, jarn.mkrelease seems more fit.

Run your tests on jenkins or travis.ci for continious integration
=================================================================

Assuming you've created unit, functional and/or doc tests for a Plone package (which you should do), the next step
is to run those test using continuous integration (CI). This means that the tests are run in a certain interval. If a test
is failing a notification is sent out by email.

If you haven't created tests for your package you can read the `'Testing and debugging' document on readthedocs <http://collective-docs.readthedocs.org/en/latest/testing_and_debugging/index.html>`_.

Two tools are available for CI in Plone, `Travis CI <https://travis-ci.org/>`_ and `Jenkins CI <http://jenkins-ci.org/>`_.

The Travis CI tool is offered as software as a service. Travis offers CI for open source projects hosted on GitHub.

Jenkins CI is a tool which can be installed on a server. Because Travis doesn't support CI for internal projects
(such as closed source/proprietary software), Jenkins CI can be used for those projects. When testing projects in Jenkins
the add-on `collective.xmltestreport <http://pypi.python.org/pypi/collective.xmltestreport>`_ can be used to output which
tests are run.
