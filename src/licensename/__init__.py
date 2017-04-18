VERSION = (0, 3)
__version__ = '.'.join(map(str, VERSION))

from .licensename import from_file, from_text
