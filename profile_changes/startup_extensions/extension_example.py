"""
Example of a simple extension that will reliably run on ipykernel startup.
and fail loudly if there's some error.
"""
# import numpy as np
# You can put your code or security guardrails startup code here.

def load_ipython_extension(ipython):
  # If you need a reference to ipython API, put the code here.
  # This function is going to be called automatically when ipython loads the file.
  pass

  # If you need to make some variables available to the user namespace, you can do it like following
  # ipython.user_ns['np'] = np

  # If you have no code here, you can delete the method.
