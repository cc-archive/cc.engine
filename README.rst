=========
cc.engine
=========

----

🛑 **As of 2023-09-27, this project was deprecated by the new CC Legal Tools**
(cc-legal-tools-app_, cc-legal-tools-data_) and Chooser_.

.. _cc-legal-tools-app: https://github.com/creativecommons/cc-legal-tools-app
.. _cc-legal-tools-data: https://github.com/creativecommons/cc-legal-tools-data
.. _Chooser: https://github.com/creativecommons/chooser

----


:Date: $LastChangedDate: 2006-11-21 11:23:54 -0500 (Tue, 21 Nov 2006) $
:Version: $LastChangedRevision: 4737 $
:Author: Nathan R. Yergler <nathan@creativecommons.org>
:Organization: `Creative Commons <http://creativecommons.org>`_
:Copyright:
   2007, Nathan R. Yergler, Creative Commons;
   licensed to the public under the Expat/`MIT
   <http://www.opensource.org/licenses/MIT>`_ License.


cc.engine provides the Creative Commons license engine along with a set of
related scripts. The scripts can be used for generating static versions of
the license deeds.


ccEngine
========

The ccEngine is comprised of the following repositories:

* cc.api_: *Legacy API to integrate the Creative Commons licensing engine into
  third party applications*
* cc.engine_ (this repository): *Python app that runs part of the license
  engine on CC's website*
* cc.i18n_: *Localization data for CC's deeds and license chooser*
* cc.license_: *Python app that runs part of the license engine on CC's
  website*
* cc.licenserdf_: *RDF describing Creative Commons licenses*
* rdfadict_: *An RDFa parser wth a simple dictionary-like interface.*

ccEngine is primarlily a Python project with 106 Python files (87.6%) across its repositories. The Python files contain:

* 7,315 lines of code (51.4%)
* 2,481 lines of comments (17.4%)

.. _cc.api:  https://github.com/cc-archive/cc.api
.. _cc.engine: https://github.com/cc-archive/cc.engine
.. _cc.i18n: https://github.com/cc-archive/cc.i18n
.. _cc.license: https://github.com/cc-archive/cc.license
.. _cc.licenserdf: https://github.com/cc-archive/cc.licenserdf
.. _rdfadict: https://github.com/cc-archive/rdfadict


WARNING
=======

Much of the documentation associated with this project is no longer accurate!


Installation
============

NOTE: Unless you are installing this in ``Development Mode``, you will need to
run ``sudo ./bin/buildout`` (with root privileges), because the script needs to
create directories in ``/etc`` and ``/var``.

cc.engine uses `zc.buildout <http://python.org/pypi/zc.buildout>`_ to
assemble the software and its dependencies. For example ::

  $ python bootstrap/bootstrap.py
  $ ./bin/buildout

After the buildout process completes the application may be started using
the generated init script ::

  # /etc/init.d/cc_engine-run-cc_engine start

You can prevent the service from detaching from the console as a daemon with
the ``fg`` argument (instead of ``start'') ::

  # /etc/init.d/cc_engine-run-cc_engine fg

If you get a UnicodeDecodeError from the cc.engine (you'll see this if it's
running in the foreground) when you try to access the http://host:9080/license/
then it's likely that the install of python you are using is set to use ASCII
as it's default output.  You can change this to UTF-8 by creating the file
/usr/lib/python<version>/sitecustomize.py and adding these lines:

  import sys
  sys.setdefaultencoding("utf-8")


Development Mode
----------------

If you are working on developing cc.engine, a special buildout configuration
is provided.  This configuration differs from the default in the following
ways:

* Zope is configured to run in ``devmode``.
* A XXX report is generated at time of buildout.

You can build cc.engine for development by specifying the buildout configuration
on the command line ::

  $ ./bin/buildout -c dev.buildout.cfg


Building lxml + Dependencies
----------------------------

cc.engine relies of `lxml <http://codespeak.net/lxml>`_, which is a Python
wrapper for libxml2 and libxslt1. If you system has older versions of these
libraries installed, cc.engine may fail with ``Unknown symbol`` errors. A
specialized buildout configuration is provided to download and build a
local version of libxml2, libxslt1 and lxml if needed. To use this, specify
the configuration on the command line ::

  $ ./bin/buildout -c lxml.buildout.cfg

Note that this builds in production mode.


Dependencies
============


Debian
------

* ``python-cssselect``

  * `GitHub - scrapy/cssselect: CSS Selectors for Python
    <https://github.com/scrapy/cssselect>`_

* ``python-flup`` (includes required patches, not available upstream)

  * `flup: random Python WSGI stuff <https://www.saddi.com/software/flup/>`_

* ``python-librdf``

  * `Redland RDF Libraries <http://librdf.org/>`_


Python
------

* `Paste Deployment — Paste Deploy 2.1.0 documentation
  <https://docs.pylonsproject.org/projects/pastedeploy/en/latest/>`_


Additional Documentation
========================

* `docs/source/tech_overview.rst <docs/source/tech_overview.rst>`_
* `docs/source/overarching_infrastructure.rst
  <docs/source/overarching_infrastructure.rst>`_
* `docs/source/history.rst <docs/source/history.rst>`_
