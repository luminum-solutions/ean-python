import django

if "1.8" in django.__version__:
    from .settings_1_8 import *
else:
    from .settings import *

from .ean_api_settings import *
