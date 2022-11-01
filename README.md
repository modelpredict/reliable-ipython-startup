# Reliable ipython startup scripts template

[Full docs and explanation](https://modelpredict.com/how-to-write-reliable-scripts-ipython/).

This is a template to reliably run some code ipython kernel startup.

**If your code fails, kernel will fail**. Something you can't get done with startup scripts.

Handy to boot Jupyter notebooks and ipython consoles with some code, e.g. for starting some security guardrails.

## Usage
1. Clone the repo
2. Copy your startup code to `profile_changes/startup_extensions/extension_example.py`. The `load_ipython_extension` function is not necessary unless you need a handle to ipython.
3. Copy both files to the default ipython profile with following command

```sh
cp -r profile_changes/* $(ipython locate)/profile_default
```
