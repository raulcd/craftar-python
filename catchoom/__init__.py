#  (C) Catchoom Technologies S.L.
#  Licensed under the MIT license.
#  https://github.com/catchoom/catchoom-python/blob/master/LICENSE
#  All warranties and liabilities are disclaimed.

"Provides access to the Catchoom APIs"

from catchoom._recognition import search
from catchoom._management import *

__version__ = (1, 0)
__versionstr__ = '.'.join([str(n) for n in __version__])
