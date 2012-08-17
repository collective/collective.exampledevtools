from five import grok

from zope.interface import Interface

class ExampleView(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    
    grok.name('example_view')

    def render(self):
        1/0

