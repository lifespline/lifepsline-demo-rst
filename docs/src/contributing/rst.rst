==========
RST Syntax
==========

Core Concepts
-------------

You'll find literature on these concepts at :doc:`../literature`

* :ref:`section header <subsection>`
* :ref:`directive <directive>`
* :ref:`role <role>`
* :ref:`reference  <role>`
* :ref:`inline external link <inline_ext_link>`
* :ref:`cross-references <cross_reference>`
* :ref:`root document <root>`
* :ref:`code-block <code>`
* :ref:`domain <domain>`

.. _root:

this is the root document


.. _domain:

Domain
------

`read the docs <https://www.sphinx-doc.org/en/master/glossary.html#term-domain>`_

.. _subsection:

Subsection header
--------------

This is a subsection header.

.. _code:

Code block
----------

.. code:: bash

    echo "this is a code block"

.. _cross_reference:

Cross-Reference
---------

.. _role:

Role
----

Roles:

* doc
* ref
* py:func

Pointing to a document in the same dir: :doc:`documentation <documentation>`.

.. _directive:

Directive
---------

Directives:

* py:function

:py:func:`mod.f` is the documentation for the python function ``mod.f()``:

.. py:function:: mod.f(arg=None)

   High-level description of what the function does/returns.

   :param arg: arg description.
   :type arg: list[str] or None
   :raise mod.InvalidArgError: reason for err description.
   :return: what the function returns.
   :rtype: list[str]

notice that the function raises an exception :py:exc:`mod.InvalidArgError`:

.. py:exception:: mod.InvalidArgError

   Raised if some condition is met.
