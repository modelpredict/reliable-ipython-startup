import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "startup_extensions"))

c.InteractiveShellApp.reraise_ipython_extension_failures = True
c.InteractiveShellApp.extensions.append(
  'extension_example'
)


