import grok
from zope.interface import implements
from zope.publisher.interfaces import NotFound
from zope.i18n import translate
from zope.i18n.interfaces import ITranslationDomain
from zope.component import queryUtility

from cc.license.decorators import memoized
from cc.engine.licenses.standard import BrowserLicense, LicenseDeed

class MitBsdLicense(BrowserLicense):
    """Browser License for MIT/BSD licenses."""

    @property
    @memoized
    def is_mit(self):
        """Return True if the context is an MIT license."""

        return "MIT" in self.license.uri

    @property
    @memoized
    def is_bsd(self):
        """Return True if the context is an BSD license."""

        return "BSD" in self.license.uri

    
class MitBsdDeed(LicenseDeed):
    grok.context(MitBsdLicense)
    grok.name('index')
    grok.template('deed')
    
