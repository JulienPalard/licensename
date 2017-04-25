=====
Usage
=====

To find the license name of a license file, this package can be used
as a script:

.. code-block:: shell-session

  $ licensename tests/licenses/MIT.txt
  MIT
  $ licensename tests/licenses/BSD-2-Clause.txt
  BSD-2-Clause

Or as a module::

.. code-block:: pycon

  >>> import licensename
  >>> licensename.from_file('./tests/licenses/MIT.txt')
  'MIT'
  >>> licensename.from_file('./tests/licenses/BSD-2-Clause.txt')
  'BSD-2-Clause'
  >>> licensename.from_text("MIT License\nyadi yadi yada…")
  'MIT'
