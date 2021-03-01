import pysbs

# Import context module from pysbs
from pysbs import context

# Creation of the context
aContext = context.Context()
# Declaration of alias 'myAlias'
aContext.getUrlAliasMgr().setAliasAbsPath(aAliasName = 'myAlias', aAbsPath = '<myAliasAbsolutePath>')