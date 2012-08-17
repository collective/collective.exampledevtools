from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class CollectiveExampledevtools(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import collective.exampledevtools
        xmlconfig.file('configure.zcml',
                       collective.exampledevtools,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        pass

COLLECTIVE_EXAMPLEDEVTOOLS_FIXTURE = CollectiveExampledevtools()
COLLECTIVE_EXAMPLEDEVTOOLS_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(COLLECTIVE_EXAMPLEDEVTOOLS_FIXTURE, ),
                       name="CollectiveExampledevtools:Integration")