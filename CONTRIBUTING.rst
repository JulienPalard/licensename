.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.


How to add a mis-detected license
---------------------------------

Known licenses are stored in
``src/licensename/known_licenses.py``. The structure is aimed to be
understandable by humans: it's a simple dict, each level of the dict
correspond to an unwrapped paragraph in the license, like::

    "APPLE PUBLIC SOURCE LICENSE": {
        "Version 1.0 - March 16, 1999": "APSL-1.0",
        "Version 1.1 - April 19,1999": "APSL-1.1",
        "Version 2.0 - August 6, 2003": "APSL-2.0"
    },
    "Academic Free License": {
        "Version 1.1": "AFL-1.1",
        "Version 1.2": "AFL-1.2"
    }

reads like: If first paragraph one is "APPLE PUBLIC SOURCE LICENSE",
and the second paragraph is "Version 1.0 - March 16, 1999", it's an
"APSL-1.0" license.

In other worlds, first dict is for paragraph one, second level of dicts are
for paragraph two, etc… until as string is found instead of a dict, meaning
there's no longer need for disambiguation, and it's the license name.

Lines containing ``(c)``, ``(C)``, empty lines, or starting with
``Copyright`` are removed before paragraph parsing.

You can easily see how ``licensename`` sees paragraphs of a license
file by trying the ``--pretty-print`` option::

    $ licensename --pretty-print tests/licenses/MIT~1.txt
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


If your paragraphs are incorrectly parsed, you can fix it in the
`textunwrap
<https://textunwrap.readthedocs.io/en/latest/index.html>`__ project.
