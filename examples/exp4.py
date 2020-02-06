import sys
from fluidasserts.lang import python

python.has_generic_exceptions(sys.modules['fluidasserts'].__path__[0])
