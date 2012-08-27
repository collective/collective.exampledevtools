********************************
Example Plone Developement Tools
********************************

.. topic:: Overview

    The :mod:`plone.api` is an elegant and simple API, built for humans wishing
    to develop with Plone.


This package is created for the Plone Conf 2012 talk, Essential Development Tools. When developing a
Plone product there are tools available which can ease development.



Introduction
============

When developing a Plone product there are tools available which can ease development. This talk will explain which tools are available and how to use them.

This egg is created for the Plone Conf 2012 talk, Essential Development Tools. When developing a Plone product
  there are tools available which can ease development.

Speed up buildout
=================

.. figure:: http://fschulze.github.com/mr.developer/xkcd-buildout.png
    :figwidth: image

    Let Mr. Developer help you win the everlasting buildout battle!

    (Remixed by Matt Hamilton, original from http://xkcd.com/303)

Use allow hosts in buildout to speed up downloading of eggs
Use a default.cfg in your buildout to centralize eggs and download caches

Also see: http://blog.aclark.net/2012/08/13/bootstrapping-a-buildout-1-6-release/

Creating buildouts and products using paster or templer


Manage development eggs with mr.developer
=========================================

.. figure:: http://fschulze.github.com/mr.developer/xkcd-buildout.png
    :figwidth: image

    Let Mr. Developer help you win the everlasting buildout battle!

    (Remixed by Matt Hamilton, original from http://xkcd.com/303)

Mr.developer helps with development eggs, auto-checkout and updating all eggs.
Other tips and tricks

Automatically restart using sauna.reload
========================================




Use Omelette to create a unified directory structure of installed packaged
==========================================================================
and 'use the source (luke)' to search in Plone core packages


Dive into pdb when an error is raised using Products.PDBDebugMode
=================================================================


Debug a frozen instance using Products.signalstack
==================================================


Do the PDB anywhere in your Plone site with Clouseau
====================================================


Ease the releasing of eggs with jarn.mkrelease or zest.mkrelease
================================================================


Run your tests on jenkins or travis.ci for continious integration
=================================================================


