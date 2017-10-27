Overview
========

Whilst looking about to see if anyone had proposed a __json__ protocol for
Python, I found `this article <https://hynek.me/articles/serialization/>`_ and
it struck me as so simple and obviously right.

So, I decided to provide a lib to make it easier for everyone.


Usage
=====

Just pass json_default.default as the default function when calling json.dump(s).


.. code-block:: python

   import json

   from json_default import default

   ...

   return json.dumps(mydata, default=default)


If you have more types you want to define serialisation for, just add them:

.. code-block:: python

   from json_default import default


   @default.register(mytype):
   def _(obj):
       ...
