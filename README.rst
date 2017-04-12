===========
licensename
===========

Module or script to find a license name from a license text or file.


Usage
=====

This can be used as a script::

  $ licensename tests/licenses/MIT.txt
  MIT
  $ licensename tests/licenses/BSD-2-Clause.txt
  BSD-2-Clause

Or as a module::

  >>> import licensename
  >>> licensename.from_file('./tests/licenses/MIT.txt')
  'MIT'
  >>> licensename.from_file('./tests/licenses/BSD-2-Clause.txt')
  'BSD-2-Clause'
  >>> licensename.from_text("MIT License\nyadi yadi yada…")
  'MIT'


Adding a license
================

Known licenses are stored in
``src/licensename/known_licenses.py``. The structure is aimed to be
understandable by humans: it's a simple dict, each level of the dict
correspond to a line in the license, like::

     "The LaTeX Project Public License": {
       "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-": {
           "LPPL Version 1.1 1999-07-10": "LPPL-1.1",
           "LPPL Version 1.2 1999-09-03": "LPPL-1.2",
           "LPPL Version 1.3a 2004-10-01": "LPPL-1.3a",
           "LPPL Version 1.3c 2008-05-04": "LPPL-1.3c"
       }
     }

reads like: If line one is "The LaTeX Project Public License", and the
line two is "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-", and the line three is
"LPPL Version 1.1 1999-07-10", it's an "LPPL-1.1", and so on.

In other worlds, first dict is for line one, second level of dicts are
for line two, etc… until as string is found instead of a dict, meaning
there's no longer need for disambiguation, and it's the license name.

Lines containing ``(c)``, ``(C)``, empty lines, or starting with
``Copyright`` are ignored.

Note
====

This project has been set up using PyScaffold 2.5.7. For details and usage
information on PyScaffold see http://pyscaffold.readthedocs.org/.
