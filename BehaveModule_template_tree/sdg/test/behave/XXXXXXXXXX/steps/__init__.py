# Export all step files in this tree to be hoovered up by the behave
# engine.

# This is so that we don't have to manually import the step file steps
# in each individual project.
# e.g.
#   from sdg.test.behave.XXXXXXXXXX.steps import *

import pkgutil

__all__ = []
for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    __all__.append(module_name)
    _module = loader.find_module(module_name).load_module(module_name)
    globals()[module_name] = _module
