from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class PlonethemeCue(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import plonetheme.cue
        xmlconfig.file('configure.zcml',
                       plonetheme.cue,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        pass

PLONETHEME_CUE_FIXTURE = PlonethemeCue()
PLONETHEME_CUE_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(PLONETHEME_CUE_FIXTURE, ),
                       name="PlonethemeCue:Integration")