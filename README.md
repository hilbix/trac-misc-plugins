# Miscellaneous Trac Plugins

These plugins are either in use by me or are written by me:

- If they are written by me, the license is [COPYRIGHT.CLL](./COPYRIGHT.CLL).
- Else not.  Probably true for all other submodules.

Have a look directly into the plugins to find out what they are for.

- No `setup.py` needed, just copy (or better softlink) them to your trac instance's `plugins/` directory.


## Usage

	git submodule add https://github.com/hilbix/trac-misc-plugins.git
	ln --relative -s trac-misc-plugins/*.py $YourTracInstance/plugins/


## FAQ

License?

- This Works is placed under the terms of the Copyright Less License,  
  see file COPYRIGHT.CLL.  USE AT OWN RISK, ABSOLUTELY NO WARRANTY.
- Read:  This is free as in free beer, free speech and free baby
- The only difference to Public Domain is, that you must not cover the code
  (or portions of it) with any Copyright before, at least, the year 2100

Contact? Bugs? Contrib? Questions?

- Open Issue or PR on GH
- Perhaps I listen

Submodules?  Subdirectories?

- This is WiP to probably more easily add all the other plugins I use
- Currently there are none, but
  - these certainly need `setup.py`
  - there will be a suitable `Makefile`
